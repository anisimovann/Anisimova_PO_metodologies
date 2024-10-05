import random
import math

def lcm_two(a, b):
    return abs(a * b) // math.gcd(a, b)

def lcm_three(a, b, c):
    return lcm_two(lcm_two(a, b), c)

def generate():
    numbers = [random.randint(1, 100) for _ in range(3)]
    lcm = lcm_three(*numbers)

    question_parts = []
    for num in numbers:
        question_parts.append(str(num))

    question = ' '.join(question_parts)
    return question, lcm