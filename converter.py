class Conversion:
    aNum = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    rNum = ["I", "V", "X", "L", "C", "D", "M"]

    def __init__(self, number):
        self.number = str(number).upper()

    def idNum(self):  # Identifies the numeral type, returns an error if input is invalid
        numbers = self.number
        aNum = str(self.aNum)
        a, r = 0, 0
        for num in numbers:
            if num in aNum:
                a += 1
            if num in self.rNum:
                r += 1

        if a == len(numbers):
            if int(numbers) > 3_999:
                return "Invalid"
            return "Arabic"
        elif r == len(numbers):
            return "Roman"
        else:
            return "Invalid"

    def arToRom(self):  # Method to convert Arabic numerals to Roman numerals

        aNum = self.number[::-1]
        result = []

        def createTable(one, five, ten):  # Function which creates a Roman numeral number table for a specific digit
            table = [one, one + one, one + one + one, one + five, five, five + one, five + one + one,
                     five + one + one + one, one + ten]
            return table

# List of lists of three arguments to pass to createTable function in order to create a digit-specific number table
        tableArgs = ["I", "V", "X"], ["X", "L", "C"], ["C", "D", "M"], ["M", " ", " "]

        for digit, i in enumerate(range(len(aNum))):

            if int(aNum[digit]) != 0:
                table = createTable(*tableArgs[i])
                result.append(table[int(aNum[digit]) - 1])

        result = ''.join(result[::-1])
        return result

    def romToAr(self): # Method to convert Roman numerals to Arabic numerals
        number = self.number[::-1]
        values = []
        result = [0]

        rChart = ["I", "V", "X", "L", "C", "D", "M"]  # Roman Numeral Chart
        aChart = ["1", "5", "10", "50", "100", "500", "1000"]  # Arabic Numeral equivalent

        for i in range(
                len(number)):  # Converts Roman Numeral Numbers to their Arabic Numeral equivalents of the integer type
            values.append(int(aChart[rChart.index(number[i])]))

        j = 0  # Iteration variable
        for value in values:
            if value < result[j]:
                if len(str(result[j])) > (len(str(value)) + 1):  # Debugging component
                    return "Invalid"
                result[j] = result[j] - value
            elif value >= result[j]:
                result.append(value)
                j += 1

        if sum(result) >= 3999:
            return "Invalid"

        return sum(result)

    def evaluate(self):
        if self.idNum() == "Arabic":
            return self.arToRom()
        elif self.idNum() == "Roman":
            return self.romToAr()
        else:
            return "Invalid"
