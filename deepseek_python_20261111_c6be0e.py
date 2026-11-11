import math
import matplotlib.pyplot as plt

print("=== Asphalt Delivery Calculator ===")
...

try:
    S = float(input("Area S, m2: ").replace(",", "."))
    ...
except ValueError:
    print("Error: enter numbers")
else:
    if any <= 0:
        print("Error: value must be > 0")
    else:
        # calc
        ...
        # plot M vs S
        S_values = list(range(100, 1001, 50))
        M_values = [Sv * (h/100) * rho for Sv in S_values]
        
        plt.figure(figsize=(9,5))
        plt.plot(S_values, M_values, color='steelblue', linewidth=2.5, marker='o', markersize=4)
        plt.scatter([S], [M], color='crimson', s=80, zorder=5, label='User value')
        plt.axvline(S, color='crimson', linestyle='--', alpha=0.6)
        
        plt.title('Mass of asphalt mix vs Area (h = {:.2f} cm, rho = {:.2f} t/m3)'.format(h, rho))
        plt.xlabel('Area S, m2')
        plt.ylabel('Mass M, t')
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.legend()
        plt.tight_layout()
        plt.show()
        
        # text summary
        max_M = max(M_values)
        max_S = S_values[M_values.index(max_M)]
        print()
        print("--- Plot summary ---")
        print(f"Range of S: {S_values[0]} - {S_values[-1]} m2, step 50")
        print(f"Minimum M: {min(M_values):.2f} t at S = {S_values[M_values.index(min(M_values))]} m2")
        print(f"Maximum M: {max_M:.2f} t at S = {max_S} m2")