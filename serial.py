"""Python serial number generator."""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        "Initialize original start number and current number"
        self.original_start_num = self.current_num = start

    def generate(self):
        "Return next sequential number every time generate () is called"
        serial = self.current_num
        self.current_num += 1
        return serial

    def reset(self):
        "Reset the number back to the original start number"
        self.current_num = self.original_start_num
