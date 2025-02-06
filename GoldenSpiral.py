from mpmath import mp

mp.dps = int(input("how many floating points you want? "))

def fibonacci_ratio(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b / a

def golden_ratio_fibonacci_approximation():
    n = 1000
    return fibonacci_ratio(n)



phi_precise = golden_ratio_fibonacci_approximation()

print(f"Golden Ratio using Fibonacci approximation with {mp.dps} decimal places:\n{phi_precise}")

