from mpmath import mp

mp.dps = int(input("how many floating points you want? "))

def fibonacci_ratio(n):
    F_n = mp.fibonacci(n)
    F_n1 = mp.fibonacci(n+1)
    return F_n1 / F_n

def golden_ratio_fibonacci_approximation():
    n = 1000
    return fibonacci_ratio(n)

phi_precise = golden_ratio_fibonacci_approximation()
print(f"Golden Ratio using Fibonacci approximation with {mp.dps} decimal places:\n{phi_precise}")
