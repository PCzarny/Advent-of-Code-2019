# https://adventofcode.com/2019/day/1

def get_required_fuel(mass):
    return mass // 3 - 2

def get_input_numbers():
    with open('input', 'r') as f:
        lines = f.readlines()
        return map(lambda line: int(line), lines)

def task1():
    inputs = get_input_numbers()
    fuel_requirements = map(lambda input: get_required_fuel(input), inputs)
    print(sum(fuel_requirements, 0))

def get_total_fuel(mass, totall_fuel):
    fuel_for_mass = get_required_fuel(mass)
    if fuel_for_mass < 0:
        return totall_fuel
    return get_total_fuel(fuel_for_mass, fuel_for_mass + totall_fuel)

def task2():
    inputs = get_input_numbers()
    fuel_requirements = map(lambda input: get_total_fuel(input, 0), inputs)
    print(sum(fuel_requirements, 0))
