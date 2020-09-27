class calculator:

    def __init__(self):
        self.what = "Calculator adalah kelas yang memiliki fungsi perhitungan"
    
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def minus(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def division(a, b):
        if a == 0 or b == 0:
            return "Can\'t divide by Zero", False
        elif a == 65 and b == 0:
            return "Infinite", False
        else:
            return a / b

    @staticmethod
    def mod(a, b):
        return a % b

if __name__ == "__main__":
    calc = calculator()
    a = calculator.division(500, 4)
    print(type(a))
    print(a)
    print(calculator.minus(1, 0))
    print(isinstance(calc, calculator))