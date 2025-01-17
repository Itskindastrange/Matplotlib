# -*- coding: utf-8 -*-
"""charts in matplotlib.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_6DUHfdo1eQXxIq344atYOipCJkboPOk
"""

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
import matplotlib
from matplotlib import pyplot as plt

plt.plot([1, 2, 3, 4],[2,7,4,8])
plt.title("Graph")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.show()

from matplotlib import style
import matplotlib.pyplot as plt

style.use("ggplot")

x0 = [1, 2, 3, 4]
y0 = [2, 7, 4, 8]
x1 = [0, 5, 10, 12]
y1 = [4, 5, 6, 7]

plt.scatter(x0, y0, label='0')
plt.plot(x1, y1, label='1')
plt.legend()
plt.show()

from matplotlib import style
import matplotlib.pyplot as plt

style.use("ggplot")

x0 = [1, 2, 3, 4]
y0 = [2, 7, 4, 8]
x1 = [0, 5, 10, 12]
y1 = [4, 5, 6, 7]


plt.plot(x0, y0, label='Line 0')
plt.plot(x1, y1, label='Line 1')


plt.scatter(x0, y0, color='blue', s=50, zorder=5)
plt.scatter(x1, y1, color='red', s=50, zorder=5)

plt.legend()
plt.show()

from matplotlib import style
import matplotlib.pyplot as plt

style.use("ggplot")

x0 = [1, 2, 3, 4]
y0 = [2, 7, 4, 8]
x1 = [0, 5, 10, 12]
y1 = [4, 5, 6, 7]


plt.plot(x0, y0, label='Line 0')
plt.plot(x1, y1, label='Line 1')


plt.scatter(x0, y0, color='blue', s=50, zorder=1.5)
plt.scatter(x1, y1, color='red', s=50, zorder=0)

plt.legend()
plt.show()

from matplotlib import style
import matplotlib.pyplot as plt

style.use("ggplot")

x0 = [1, 2, 3, 4]
y0 = [2, 7, 4, 8]
x1 = [0, 5, 10, 12]
y1 = [4, 5, 6, 7]

# Plotting the lines with default zorder
plt.plot(x0, y0, label='Line 0', zorder=1)
plt.plot(x1, y1, label='Line 1', zorder=1)

# Plotting the dots with higher zorder
plt.scatter(x0, y0, color='blue', s=50, zorder=2)  # zorder=2 to ensure dots are on top
plt.scatter(x1, y1, color='red', s=50, zorder=2)

# Setting axis limits
plt.xlim(-2, 14)  # Set x-axis limits
plt.ylim(0, 10)   # Set y-axis limits

# Customizing the ticks
plt.xticks(range(-2, 15, 2))  # Set x-axis ticks from -2 to 14 with a step of 2
plt.yticks(range(0, 11, 1))   # Set y-axis ticks from 0 to 10 with a step of 1

plt.legend()
plt.show()

from matplotlib import style
import matplotlib.pyplot as plt

style.use("ggplot")

x0 = [1, 2, 3, 4]
y0 = [2, 7, 4, 8]
x1 = [0, 5, 10, 12]
y1 = [4, 5, 6, 7]

# Plotting the lines with default zorder
plt.plot(x0, y0, label='Line 0', zorder=1)
plt.plot(x1, y1, label='Line 1', zorder=1)

# Plotting the dots with higher zorder
plt.scatter(x0, y0, color='blue', s=50, zorder=2)  # zorder=2 to ensure dots are on top
plt.scatter(x1, y1, color='red', s=50, zorder=2)

plt.axis("off")

plt.legend()
plt.show()

from matplotlib import style
import matplotlib.pyplot as plt
import numpy as np

style.use("ggplot")

# Create some sample data
x0 = [1, 2, 3, 4]
y0 = [2, 7, 4, 8]
x1 = [0, 5, 10, 12]
y1 = [4, 5, 6, 7]

# Create a random image
image = np.random.rand(10, 10)

# Display the image
plt.imshow(image, extent=[-2, 14, 0, 10], aspect='auto')

# Plotting the lines with default zorder
plt.plot(x0, y0,color='pink', label='Line 0', zorder=1)
plt.plot(x1, y1, label='Line 1', zorder=1)

# Plotting the dots with higher zorder
plt.scatter(x0, y0, color='blue', s=50, zorder=2)  # zorder=2 to ensure dots are on top
plt.scatter(x1, y1, color='red', s=50, zorder=2)

# Adding a legend
plt.legend()
#plt.axis('off')
plt.show()

import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D']
values = [4, 7, 1, 8]

plt.bar(categories, values, color='green')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Basic Bar Plot')
plt.show()

import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(1000)

plt.hist(data, bins=100, color='purple')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Basic Histogram')
plt.show()

import matplotlib.pyplot as plt

labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]

plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title('Basic Pie Chart')
plt.show()

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.plot(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Plot with Annotations')
plt.annotate('Highest point', xy=(5, 11), xytext=(3, 10),
             arrowprops=dict(facecolor='black', shrink=0.05))
plt.show()

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [2, 3, 5, 7, 11]
y2 = [1, 4, 9, 16, 25]

fig, (ax1, ax2) = plt.subplots(1, 2)

ax1.plot(x, y1)
ax1.set_title('Subplot 1')

ax2.plot(x, y2)
ax2.set_title('Subplot 2')

plt.suptitle('Subplots Example')
plt.show()

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.plot(x, y, linestyle='--', color='magenta', marker='o')
plt.xlabel('X-axis', fontsize=14, color='blue')
plt.ylabel('Y-axis', fontsize=14, color='blue')
plt.title('Customized Plot', fontsize=18, color='red')
plt.grid(True)
plt.show()

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.plot(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Plot to Save')
plt.savefig('my_plot.png')  # Save as PNG file
plt.savefig('my_plot.pdf')  # Save as PDF file
plt.show()

