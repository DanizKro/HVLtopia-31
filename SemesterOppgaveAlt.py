import numpy as np
import matplotlib.pyplot as plt
from random import randint


# Generate random data for a year
def GenereateRandomYearDataList(intencity: float, seed: int = 0) -> list[int]:
    if seed != 0:
        np.random.seed(seed)
    centervals = [200, 150, 100, 75, 75, 75, 50, 75, 100, 150, 200, 250, 300]
    centervals = [x * intencity for x in centervals]
    nox = centervals[0]
    inc = True
    noxList = []
    for index in range(1, 365):
        if randint(1, 100) > 50:
            inc = not inc
        center = centervals[int(index / 30)]
        dx = min(2.0, max(0.5, nox / center))
        nox = nox + randint(1, 5) / dx if inc else nox - randint(1, 5) * dx
        nox = max(10, nox)
        noxList.append(nox)
    return noxList


# Generate data for NOx and Asphalt dust for different locations
kron_nox_year = GenereateRandomYearDataList(intencity=1.0, seed=2)
nord_nox_year = GenereateRandomYearDataList(intencity=0.3, seed=1)
bryggen_nox_year = GenereateRandomYearDataList(intencity=1, seed=3)

kron_asfaltstov_year = GenereateRandomYearDataList(intencity=2, seed=4)
nord_asfaltstov_year = GenereateRandomYearDataList(intencity=4, seed=5)
bryggen_asfaltstov_year = GenereateRandomYearDataList(intencity=3, seed=6)

# Define the quarter or full year selection
quarterYear = int(input("Kvartal 1-4  (0=Hele Året)  : "))

if quarterYear == 0:
    startDag = int(input("Skriv inn start dag (f.eks. 1-360): "))
    sluttDag = int(input("Skriv inn slutt dag (f.eks. 1-360): "))


# Function to set intervals based on user input
def get_interval():
    if quarterYear == 0:
        xlabels = ['J', 'F', 'M', 'A', 'M', 'J', 'J', 'A', 'S', 'O', 'N', 'D']
        month_starts = [0, 30, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]
        xticks = np.array(month_starts)
        days_interval = (0, 360)
        xticks = np.append(xticks, [startDag, sluttDag])
        xlabels += [str(startDag), str(sluttDag)]
    elif quarterYear == 1:
        xticks = [15, 45, 75]
        xlabels = ['Jan', 'Feb', 'Mars']
        days_interval = (0, 90)
    elif quarterYear == 2:
        xticks = [15, 45, 75]
        xlabels = ['April', 'Mai', 'Juni']
        days_interval = (90, 180)
    elif quarterYear == 3:
        xticks = [15, 45, 75]
        xlabels = ['July', 'Aug', 'Sept']
        days_interval = (180, 270)
    elif quarterYear == 4:
        xticks = [15, 45, 75]
        xlabels = ['Okt', 'Nov', 'Des']
        days_interval = (270, 360)

    return days_interval, xticks, xlabels


# Plot graphs for NOx and Asphalt dust in separate subplots
def plot_graph():
    days_interval, xticks, xlabels = get_interval()

    # Set up subplots for NOx and Asphalt dust
    fig, (axNox, axAsfalt) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)
    fig.patch.set_facecolor('lightblue')

    # NOx Data
    nord_nox = nord_nox_year[days_interval[0]:days_interval[1]]
    kron_nox = kron_nox_year[days_interval[0]:days_interval[1]]
    bryggen_nox = bryggen_nox_year[days_interval[0]:days_interval[1]]
    days = len(nord_nox)
    list_days = np.linspace(1, days, days)

    axNox.plot(list_days, nord_nox, 'blue', linewidth=2, label="Nordnes")
    axNox.plot(list_days, kron_nox, 'red', linewidth=2, label="Kronstad")
    axNox.plot(list_days, bryggen_nox, 'green', linewidth=2, label="Bryggen")
    axNox.set_title("NOX nivåer" if quarterYear == 0 else f"NOx Levels - Quarter {quarterYear}")
    axNox.set_xticks(xticks)
    axNox.set_xticklabels(xlabels)
    axNox.grid(linestyle='--')
    axNox.legend()

    # Add vertical lines if full year interval is selected
    if quarterYear == 0:
        axNox.axvline(x=startDag, color='red', linestyle='--', label=f'Start: {startDag}')
        axNox.axvline(x=sluttDag, color='red', linestyle='--', label=f'Slutt: {sluttDag}')
        axNox.legend()

    # Asphalt Dust Data
    nord_asfaltstov = nord_asfaltstov_year[days_interval[0]:days_interval[1]]
    kron_asfaltstov = kron_asfaltstov_year[days_interval[0]:days_interval[1]]
    bryggen_asfaltstov = bryggen_asfaltstov_year[days_interval[0]:days_interval[1]]

    axAsfalt.plot(list_days, nord_asfaltstov, 'blue', linewidth=2, label="Nordnes")
    axAsfalt.plot(list_days, kron_asfaltstov, 'red', linewidth=2, label="Kronstad")
    axAsfalt.plot(list_days, bryggen_asfaltstov, 'green', linewidth=2, label="Bryggen")
    axAsfalt.set_title("Asfaltlstøv nivåer" if quarterYear == 0 else f"Asphalt Dust Levels - Quarter {quarterYear}")
    axAsfalt.set_xticks(xticks)
    axAsfalt.set_xticklabels(xlabels)
    axAsfalt.grid(linestyle='--')
    axAsfalt.legend()

    plt.tight_layout()
    plt.show()


plot_graph()
