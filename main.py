def input_sides():
    a = float(input("Введите длину стороны a: "))
    b = float(input("Введите длину стороны b: "))
    c = float(input("Введите длину стороны c: "))
    return a, b, c

def calculate_semiperimeter(a, b, c):
    return (a + b + c) / 2

def calculate_area(a, b, c):
    s = calculate_semiperimeter(a, b, c)
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area

if __name__ == '__main__':
    pass