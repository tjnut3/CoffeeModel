import matplotlib.pyplot as plt
import numpy as np

# Data from the classification report
classes = ['A', 'AA', 'AAA', 'B', 'Pea berry', 'เม็ดซัก', 'เม็ดซักฝอย', 'เม็ดค่า', 'เม็ดมอสาร', 'เม็ดสามเหลี่ยม', 'เม็ดหูร้าง', 'เม็ดเฟด']
precision = [0.68, 0.68, 0.81, 0.66, 0.80, 0.86, 0.92, 1.00, 0.92, 0.96, 0.85, 0.58]
recall = [0.97, 0.68, 0.98, 0.98, 0.73, 0.60, 0.82, 0.67, 0.60, 0.42, 0.93, 0.88]
f1_score = [0.80, 0.68, 0.89, 0.79, 0.77, 0.71, 0.87, 0.80, 0.73, 0.58, 0.89, 0.70]

x = np.arange(len(classes))  # the label locations
width = 0.2  # the width of the bars

fig, ax = plt.subplots(figsize=(12, 6))
rects1 = ax.bar(x - width, precision, width, label='Precision')
rects2 = ax.bar(x, recall, width, label='Recall')
rects3 = ax.bar(x + width, f1_score, width, label='F1-Score')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_xlabel('Classes')
ax.set_ylabel('Scores')
ax.set_title('Classification Report by Class')
ax.set_xticks(x)
ax.set_xticklabels(classes, rotation=45, ha='right')
ax.legend()

fig.tight_layout()

plt.show()