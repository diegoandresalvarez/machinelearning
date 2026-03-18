import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

def f(x, a, b):
    return a * np.tanh(b*x)

def df2dx2(x, a, b):
    return -2 * a * b**2 * (1/np.cosh(b*x))**2 * np.tanh(b*x)

def df3dx3(x, a, b):
    return 4*a*b**3 * (1/np.cosh(b*x))**2 * np.tanh(b*x)**2 - (2*a*b**3)*(1/np.cosh(b*x))**4

def equations(vars):
    a, b = vars
    eq1 =      f(+1, a, b) - 1 # f(+1)    = +1
    eq2 = df3dx3(+1, a, b)     # f'''(+1) = 0
    return [eq1, eq2]

# Initial guess for [a, b]
initial_guess = [1.8, 0.5]

# Solve the nonlinear system
solution = fsolve(equations, initial_guess)
a, b = solution
#a = 1.7159
#b = 2/3

print(f"Optimal values:")
print(f"a = {a:.8f}")
print(f"b = {b:.8f}")

# Verify the solution
print(f"\nVerification:")
print(f"f(+1)    = {     f(+1, a, b):+10.5f} (target: 1)")
print(f"f'''(+1) = {df3dx3(+1, a, b):+10.5f} (target: 0)")


print('''
LeCun approximated b = 0.65847895 to 2/3 = 0.66666 for convenience. Therefore:
f(+1) = a*tahn(b*1) = a*tahn((2/3)*1) = 1
and then a = 1/tanh((2/3)*1)''')
LCb = 2/3
LCa = 1/np.tanh(LCb)
print("LeCun's a =", LCa)
print("LeCun's b =", LCb)

# Plot the function and its second derivative
x = np.linspace(-5, 5, 1000)
f     = a*np.tanh(b*x)
d2f   = df2dx2(x, a, b)
LCf   = LCa*np.tanh(LCb*x)
LCd2f = df2dx2(x, LCa, LCb)


plt.figure(figsize=(12, 8))
plt.subplot(2, 1, 1)
plt.plot(x, f,   label=f'f(x) = {a:.3f}*tanh({b:.3f}*x)')
plt.plot(x, LCf, label=f'f(x) = {LCa:.3f}*tanh({LCb:.3f}*x)')
plt.axvline(x=-1, color='r', linestyle='--', alpha=0.7, label='x = ±1')
plt.axvline(x=+1, color='r', linestyle='--', alpha=0.7)
plt.grid(True, alpha=0.3)
plt.ylabel('f(x)')
plt.legend()
plt.title('Function f(x) = a*tanh(b*x)')

plt.subplot(2, 1, 2)
plt.plot(x, d2f,   label=f"f''(x)")
plt.plot(x, LCd2f, label=f"LeCun's f''(x)")
plt.axvline(x=-1, color='r', linestyle='--', alpha=0.7)
plt.axvline(x=+1, color='r', linestyle='--', alpha=0.7)
plt.grid(True, alpha=0.3)
plt.ylabel("f''(x)")
plt.xlabel('x')
plt.legend()
plt.tight_layout()
plt.show()
