import random
import math
import matplotlib.pyplot as plt

n = int(input("Enter number of steps (n > 0): "))
K = int(input("No of cycles: "))
r = int(input("No of particles per graph: "))

for cycle in range(K):

    for particle in range(r):

        # Initial position
        x, y = 0, 0
        x_path = [x]
        y_path = [y]

        # Random walk
        for i in range(n):
            direction = random.choice(
                ["up", "down", "left", "right", "diagonal", "hexagon", "chaotic"]
            )

            if direction == "up":
                y += 1
            elif direction == "down":
                y -= 1
            elif direction == "right":
                x += 1
            elif direction == "left":
                x -= 1
            elif direction == "diagonal":
                x += random.choice([-1,1]) / math.sqrt(2)
                y += random.choice([-1,1]) / math.sqrt(2)
            elif direction == "hexagon":
                a = random.randrange(6)*math.pi / 3
            elif direction == "chaotic":
                x += random.choice([-2,2])
                y += random.choice([-2,2])
           
            x_path.append(x)
            y_path.append(y)

        # Plot particle trajectory
        plt.plot(x_path, y_path, linewidth=0.8)

        # Final displacement
        distance = (x**2 + y**2) ** 0.5
        print(f"\nCycle {cycle + 1}, Particle {particle + 1}")
        print(f"Final position: ({x:.2f}, {y:.2f})")
        print(f"Distance from origin: {distance:.2f}")

    # Plot all particles in this cycle together
    plt.scatter(0, 0, color="green", label="Start")
    plt.xlabel("X position")
    plt.ylabel("Y position")
    plt.title(f"Random Walk — Cycle {cycle + 1} ({r} particles)")
    plt.grid(True)
    plt.legend()
    plt.axis("equal")
    plt.show()
