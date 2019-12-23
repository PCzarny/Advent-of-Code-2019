# https://adventofcode.com/2019/day/2
import array as arr

def load_data():
    with open('input', 'r') as f:
        content = f.read()
        return arr.array('i', map(lambda code: int(code), content.split(',')))

class Decoder:
    code = None
    next_operation_index = 0

    def __init__(self, noun, verb):
        self.load_data()
        self.restore_error(noun, verb)

    def load_data(self):
        with open('input', 'r') as f:
            content = f.read()
            self.code = arr.array('i', map(lambda code: int(code), content.split(',')))
            return self.code

    def restore_error(self, noun, verb):
        self.code[1] = noun
        self.code[2] = verb

    def get_next_operation(self):
        operation_start = self.next_operation_index
        self.next_operation_index += 4
        return self.code[operation_start : operation_start + 4]

    def add(self, operation):
        item1 = self.code[operation[1]]
        item2 = self.code[operation[2]]

        self.code[operation[3]] = item1 + item2

    def multiply(self, operation):
        item1 = self.code[operation[1]]
        item2 = self.code[operation[2]]

        self.code[operation[3]] = item1 * item2

    def run(self):

        while True:
            operation = self.get_next_operation()

            if operation[0] == 1:
                self.add(operation)
            elif operation[0] == 2:
                self.multiply(operation)
            elif operation[0] == 99:
                break
            else:
                raise Exception('invalid param')

        return self.code[0]

def task1():
    d = Decoder(12, 2)
    print(d.run())

def task2():
    expected_output = 19690720

    for noun in range(0, 100):
        for verb in range(0, 100):
            d = Decoder(noun, verb)
            result = d.run()
            if result == expected_output:
                print(100 * noun + verb)
                break
        else:
            continue
        break
