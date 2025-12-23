def area(length, width):
    """
    Функция вычисляет площадь прямоугольника
    """
    if length < 0 or width < 0:
        raise ValueError("Стороны прямоугольника не могут быть отрицательными")
    return length * width


def perimeter(length, width):
    """
    Функция вычисляет периметр прямоугольника
    """
    if length < 0 or width < 0:
        raise ValueError("Стороны прямоугольника не могут быть отрицательными")
    return 2 * (length + width)