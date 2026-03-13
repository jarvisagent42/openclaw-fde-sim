import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

sns.set_style("darkgrid")
colors = ['#0a2540', '#00d4aa', '#1e3a5f']

# Mock Tab1 Upload
fig, ax = plt.subplots(figsize=(14, 9))
ax.text(0.5, 0.6, '🛡️ Palantir FDE Simulator', fontsize=32, ha='center', va='center', fontweight='bold', color='white')
ax.text(0.5, 0.45, '📊 Dataset ETL Sim', fontsize=28, ha='center', va='center', color='#00d4aa', fontweight='bold')
ax.text(0.5, 0.3, 'Upload a CSV or JSON file', fontsize=24, ha='center', va='center', color='white')
ax.text(0.5, 0.15, 'Choose a CSV or JSON file', fontsize=20, ha='center', va='center', color='#a0a0a0', style='italic')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')
fig.patch.set_facecolor('#0a2540')
ax.set_facecolor('#0a2540')
plt.savefig('marketing_assets/mock-upload.png', bbox_inches='tight', dpi=150, facecolor='#0a2540', edgecolor='none')
plt.close()

# Mock Preview & Schema
fig, axs = plt.subplots(1, 2, figsize=(18, 9))
mock_data = np.random.rand(10, 5) * 100
sns.heatmap(mock_data, annot=True, cmap='viridis', ax=axs[0])
axs[0].set_title('Raw Data Preview (10 rows)', fontsize=20, color='white', fontweight='bold')
axs[0].set_facecolor('#1e3a5f')

axs[1].text(0.5, 0.7, 'Schema Info', fontsize=24, ha='center', va='center', fontweight='bold', color='white')
axs[1].text(0.5, 0.5, 'columns: date, sales, region, category\\ndtypes: [date, float64, str, str]\\nshape: (1000, 4)', fontsize=18, ha='center', va='center', color='#00d4aa')
axs[1].axis('off')
axs[1].set_facecolor('#0a2540')
fig.patch.set_facecolor('#0a2540')
plt.savefig('marketing_assets/mock-preview.png', bbox_inches='tight', dpi=150, facecolor='#0a2540')
plt.close()

# Mock ETL Summary
fig, ax = plt.subplots(figsize=(14, 9))
ax.text(0.5, 0.5, 'ETL Insights (Polars describe())\\nmean: 150.2\\nstd: 45.3\\nmin: 10\\nmax: 300', fontsize=22, ha='center', va='center', color='white', fontweight='bold')
ax.text(0.5, 0.3, '🚀 Ready for DuckDB Query Sim', fontsize=24, ha='center', va='center', color='#00d4aa')
ax.axis('off')
ax.set_facecolor('#1e3a5f')
fig.patch.set_facecolor('#0a2540')
plt.savefig('marketing_assets/mock-etl.png', bbox_inches='tight', dpi=150, facecolor='#0a2540')
plt.close()

# Mock Viz
x = np.linspace(0, 10, 100)
y1 = np.sin(x) * 100 + 150
y2 = np.cos(x) * 50 + 120
plt.figure(figsize=(14, 9))
plt.plot(x, y1, label='Sales', color='#00d4aa', linewidth=4)
plt.plot(x, y2, label='Trend', color='#a0a0a0', linewidth=3)
plt.title('Auto-Viz: Line Chart', fontsize=28, color='white', fontweight='bold', pad=20)
plt.xlabel('Time', fontsize=20, color='white')
plt.ylabel('Value', fontsize=20, color='white')
plt.legend(fontsize=18, facecolor='#1e3a5f', edgecolor='white')
plt.gca().set_facecolor('#1e3a5f')
plt.gcf().patch.set_facecolor('#0a2540')
plt.savefig('marketing_assets/mock-viz.png', bbox_inches='tight', dpi=150, facecolor='#0a2540')
plt.close()

# Mock Tab2
fig, ax = plt.subplots(figsize=(14, 9))
ax.text(0.5, 0.6, '📚 FDE Case Studies', fontsize=32, ha='center', va='center', fontweight='bold', color='white')
ax.text(0.5, 0.4, 'Example: Fraud Detection Pipeline\\nUpload transaction CSV, query anomalies with DuckDB', fontsize=22, ha='center', va='center', color='#00d4aa')
ax.axis('off')
ax.set_facecolor('#0a2540')
fig.patch.set_facecolor('#0a2540')
plt.savefig('marketing_assets/mock-case-studies.png', bbox_inches='tight', dpi=150, facecolor='#0a2540')
plt.close()

# Mock Tab3
fig, ax = plt.subplots(figsize=(14, 9))
ax.text(0.5, 0.6, '🎤 Interview Mocks', fontsize=32, ha='center', va='center', fontweight='bold', color='white')
ax.text(0.5, 0.45, 'Q1: Design ETL for CDP\\nA: Polars for transform, DuckDB query engine...', fontsize=22, ha='center', va='center', color='#00d4aa')
ax.axis('off')
ax.set_facecolor('#0a2540')
fig.patch.set_facecolor('#0a2540')
plt.savefig('marketing_assets/mock-interview.png', bbox_inches='tight', dpi=150, facecolor='#0a2540')
plt.close()

print("Mock screenshots generated!")