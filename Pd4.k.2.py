import random
import math
import matplotlib.pyplot as plt

plt.rcParams['figure.dpi'] = 1024

n = int(input("Enter number of steps (n > 0): "))
K = int(input("No of cycles: "))
r = int(input("No of particles per graph: "))

for cycle in range(K):

    for particle in range(r):

        # Initial position
        x, y = 0, 0
        x_path = [x]
        y_path = [y]

        for i in range(n):
            direction = random.choice(
                ["up", "down", "left", "right", "diagonal", "hexagon", "chaotic", "k1", "k2", "k3", "k4", "k5", "k6", "k7", "k8"]
            )
            
            mult = random.choice([1, 2])

            if direction == "up":
                y += 1 * mult
            elif direction == "down":
                y -= 1 * mult
            elif direction == "right":
                x += 1 * mult
            elif direction == "left":
                x -= 1 * mult
            elif direction == "diagonal":
                x += (random.choice([-1,1]) / math.sqrt(2)) * mult
                y += (random.choice([-1,1]) / math.sqrt(2)) * mult
            elif direction == "hexagon":
                a = random.randrange(6)*math.pi / 3
                x += math.cos(a) * mult
                y += math.sin(a) * mult
            elif direction == "chaotic":
                x += random.choice([-1.25,1.25]) * mult
                y += random.choice([-1.25,1.25]) * mult
              
            elif direction == "k1":
                y += 2
                x -= 1
            elif direction == "k2":
                y += 2
                x += 1
            elif direction == "k3":
                x += 2
                y += 1
            elif direction == "k4":
                x += 2
                y -= 1
            elif direction == "k5":
                x -= 2 
                y += 1
            elif direction == "k6":
                x -= 2
                y -= 1
            elif direction == "k7":
                x += 1
                y -= 2
            elif direction == "k8":
                x -= 1
                y -= 2

            x_path.append(x)
            y_path.append(y)

        # Plot particle trajectory
        plt.plot(x_path, y_path, linewidth=0.8)

        # Final displacement
        distance = (x**2 + y**2) ** 0.5
        print(f"\nCycle {cycle + 1}, Particle {particle + 1}")
        print(f"Final position: ({x:.2f}, {y:.2f})")
        print(f"Distance from origin: {distance:.2f}")

    plt.scatter(0, 0, color="green", label="Start")
    plt.xlabel("X position")
    plt.ylabel("Y position")
    plt.title(f"Random Walk — Cycle {cycle + 1} ({r} particles)")
    plt.grid(True)
    plt.legend()
    plt.axis("equal")
    plt.show()
