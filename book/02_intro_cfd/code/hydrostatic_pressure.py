import numpy as np
import matplotlib.pyplot as plt

g = 9.81
def analytical_p(h):
    return (1000 * h + h**2 / 2) * g
    
def rho(h):
    return 1000.0 + h
    
H = 400.0
N = 20

p = np.zeros(N)
dh = H / (N - 1)

for i in range(1, N):
    h = i * dh
    p[i] = p[i-1] + rho(h) * g * dh
    
print("%f"%p[N-1])
plt.gca().invert_yaxis()
height = np.linspace(0.0, H, N)

plt.plot(p, height, "o", label="Numerical", ms=8)
plt.plot(analytical_p(height), height, "-", lw=3, label="Analytical")

plt.xlabel("$p$", fontsize=20)
plt.ylabel("$h$", fontsize=20)

plt.grid()
plt.legend(loc="best")

plt.savefig("pressure.png")
plt.show()
