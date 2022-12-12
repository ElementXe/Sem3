import numpy as np
import matplotlib.pyplot as plt
import math as math

with open("students.txt") as f:
    lines = f.readlines()

studs = []
for line in lines:
    studs.append(line.split(';'))

labels = ["751", "752", "753", "754", "755", "756", ""]
mrks = np.zeros((9, 7))

for stud in studs:
    mrks[int(stud[2]) - 3][int(stud[1]) - 751] += 1

fig, ax = plt.subplots()
width = 0.7

ax.bar(labels, mrks[0], width, label='3')
ax.bar(labels, mrks[1], width, bottom=mrks[0], label='4')
ax.bar(labels, mrks[2], width, bottom=mrks[0] + mrks[1], label='5')
ax.bar(labels, mrks[3], width, bottom=mrks[0] + mrks[1] + mrks[2], label='6')
ax.bar(labels, mrks[4], width, bottom=mrks[0] + mrks[1] + mrks[2] + mrks[3], label='7')
ax.bar(labels, mrks[5], width, bottom=mrks[0] + mrks[1] + mrks[2] + mrks[3] + mrks[4], label='8')
ax.bar(labels, mrks[6], width, bottom=mrks[0] + mrks[1] + mrks[2] + mrks[3] + mrks[4] + mrks[5], label='9')
ax.bar(labels, mrks[7], width, bottom=mrks[0] + mrks[1] + mrks[2] + mrks[3] + mrks[4] + mrks[5] + mrks[6], label='10')
plt.legend(fontsize=10)

plt.title("Marks for group", fontsize=16)
plt.savefig(f"mpl_e3_graphs/marks_for_group")