import math
import numpy as np


def f(x):
    return 6*x**4 + 8*x**3 - 24*x**2 - 7

eps = 0.0001

def find_segments():
    search_range = np.arange(-10, 10, 1)
    
    a = None
    previous_x = None
    current_x = None
    segments = []
    
    for x in search_range:
        x = round(x, 4)
        current_x = f(x)
        if previous_x is not None and previous_x * current_x < 0:
            segments.append((a, x))
        a = x
        previous_x = current_x
    
    return segments

def bisection(f, a, b, eps):
    if f(a) * f(b) >= 0:
        raise ValueError("Функція не змінює знак на цьому відрізку [a, b]")
    
    while (b - a) / 2 > eps:
        c = (a + b) / 2
        if f(c) == 0:
            return c  # Знайдено корінь
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    
    return (a + b) / 2

def chord_method(f, a, b, eps):
    if f(a) * f(b) >= 0:
        raise ValueError("Функція не змінює знак на цьому відрізку [a, b]")
    
    while abs(b - a) > eps:
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        if f(c) == 0:
            return c  # Знайдено корінь
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    
    return (a + b) / 2

segments = find_segments()

for segment in segments:
    a, b = segment
    bisection_root = bisection(f, a, b, eps)
    chord_root = chord_method(f, a, b, eps)
    print(f"Корінь на відрізку [{a}, {b}] методом половинного ділення: {bisection_root}")
    print(f"Корінь на відрізку [{a}, {b}] методом хорд: {chord_root}")
