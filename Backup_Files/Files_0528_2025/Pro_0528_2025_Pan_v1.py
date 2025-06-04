import numpy as np
import matplotlib.pyplot as plt

def mse_line(x, t, w):
    y = w[0] * x + w[1]
    mse = np.mean((y - t) ** 2)
    return mse

np.random.seed(seed=1)
X_min, X_max = 4, 30
N = 16
X = 5 + 25 * np.random.rand(N)
prm = [170, 108, 0.2]
T = prm[0] - prm[1] * np.exp(-prm[2] * X) + 4 * np.random.randn(N)
# np.savez(
#     "./Backup_Related/bcp_0528_2025_v1/ch5_data.npz",
#          X = X, T = T, X_min = X_min, X_max = X_max, N = N
#          )

# print(np.round(X, 2))
# print(np.round(T, 2))

# plt.figure(figsize=(4, 4))
# plt.plot(
#     X,
#     T,
#     "blue",
#     marker = "o",
#     linestyle = "None",
#     markeredgecolor = "black"
# )
# plt.xlim(X_min, X_max)
# plt.grid()
# plt.show()

w0_n, w1_n = 100, 100
w0_min, w0_max = -25, 25
w1_min, w1_max = 120, 170
w0 = np.linspace(w0_min, w0_max, w0_n)
w1 = np.linspace(w1_min, w1_max, w1_n)
J = np.zeros((w1_n, w0_n))
for i0 in range(w0_n):
    for i1 in range(w1_n):
        w = np.array([w0[i0], w1[i1]])
        J[i1, i0] = mse_line(X, T, w)
ww0, ww1 = np.meshgrid(w0, w1)

plt.figure(figsize=(9.5, 4))
plt.subplots_adjust(wspace=0.5)
ax = plt.subplot(1, 2, 1, projection="3d")
ax.plot_surface(
    ww0, ww1, J,
    rstride = 10, cstride = 10, alpha = 0.3, color = "blue", edgecolor = "black"
)
ax.set_xticks([-20, 0, 20])
ax.set_yticks([120, 140, 160])
ax.view_init(20, -60)

plt.subplot(1, 2, 2)
cont = plt.contour(
    ww0, ww1, J, colors = "black",
    levels = [100, 1000, 10000, 100000]
)
cont.clabel(fmt = "%d", fontsize = 8)
plt.grid()
plt.show()