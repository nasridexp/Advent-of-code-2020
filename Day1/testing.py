from functools import reduce
from typing import Iterable
import operator

# read data
with open("Day1/data.txt") as datafile:
    data = [int(line.rstrip()) for line in datafile]

# year to input
total_sum = 2020

def prod(iterable: Iterable[float]) -> float:
    return reduce(operator.mul, iterable, 1)

def find_a_pair(total: int) -> (int, int):
    if total % 2 == 0:
        pair_to_find = [int(total/2), int(total/2)]
    else:
        pair_to_find = [int(total/2), int(total/2) + 1]

    found = False
    while pair_to_find[1] > 0:
        if pair_to_find[0] in data:
            data.remove(pair_to_find[0])
            if pair_to_find[1] in data:
                found = True
                break
            else:
                data.append(pair_to_find[0])
        pair_to_find[0] += 1
        pair_to_find[1] -= 1

    if found:
        return pair_to_find
    else:
        return None

pair_found = find_a_pair(total_sum)
print("Part one: The answer is {}*{}={}".format(*pair_found, pair_found[0]*pair_found[1]))

def find_a_trio(total: int) -> (int, int, int):
    third_val = total

    while third_val>0:
        if third_val in data:
            # If third value in data find a number combination that adds up to total
            # with that third value and two other numbers
            pair = find_a_pair(total_sum - third_val)
            if pair:
                break
            else:
                third_val -= 1
        else:
            third_val -=1

    return pair[0], pair[1], third_val

trio_found = find_a_trio(total_sum)
print("Part two the answer is {}*{}*{}={}".format(*trio_found, trio_found[0]*trio_found[1]*trio_found[2]))