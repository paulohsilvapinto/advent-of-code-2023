from collections import namedtuple

from commons.utils import extract_numbers
from commons.utils import read_input

Race = namedtuple("Race", ["time", "record_distance"])


def calculate_distance(time_holding, time_available):
    return time_holding * (time_available - time_holding)


races = read_input(day_number=6)
races_time = int("".join(extract_numbers(races[0], type=str)))
races_distance = int("".join(extract_numbers(races[1], type=str)))
race = Race(races_time, races_distance)
# print(race)

ways_to_beat = 0
for time_holding in range(0, race.time):
    started_winning = None
    if calculate_distance(time_holding, time_available=race.time) > race.record_distance:
        started_winning = True
        ways_to_beat += 1
    elif started_winning is False:
        break

print(ways_to_beat)
