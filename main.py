def input_sides():
    """
    Принимаем значения 3-х сторон
    :return: стороны трекгольника
    """
    a = float(input("Введите длину стороны a: "))
    b = float(input("Введите длину стороны b: "))
    c = float(input("Введите длину стороны c: "))
    return a, b, c

def calculate_semiperimeter(a, b, c):
    """
    Вычисляем полупериметр
    :param a: Сторона а
    :param b: Сторона b
    :param c: Сторона c
    :return: полупериметр
    """
    return (a + b + c) / 2

def calculate_area(a, b, c):
    """
    Вычисляем площадь трегольника
    :param a: Сторона а
    :param b: Сторона b
    :param c: Сторона c
    :return: Площадь
    """
    s = calculate_semiperimeter(a, b, c)
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area

if __name__ == '__main__':
    a, b, c = input_sides()
    area = calculate_area(a, b, c)
    print(f"Площадь треугольника равна {area}")