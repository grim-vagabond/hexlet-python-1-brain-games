#!/usr/bin/env python3
from random import randint


def brain_gcd():
    operand_one = randint(1, 100)
    operand_two = randint(1, 100)
    question = f'{operand_one} {operand_two}'
    for divisor in range(max(operand_one, operand_two), 0, -1):
        if (operand_one % divisor == 0 and operand_two % divisor == 0):
            correct_answer = divisor
            return (question, str(correct_answer))
