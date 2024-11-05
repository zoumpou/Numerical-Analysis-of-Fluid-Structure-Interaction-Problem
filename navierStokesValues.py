import matplotlib.pyplot as plt
import os

# Correct base path for Windows
base_path = r'C:\Users\mario\Desktop\αποτελεσματα\Results_FSI\αλλαγες στη γεωμετρια'

# Different test directories
test_dirs = ['δοκιμη 1 0.25_5_3', 'δοκιμη 2 0.5_5_3', 'δοκιμη 3 0.25_5_1', 
             'δοκιμη 4 0.5_5_1', 'δοκιμη 5 0.25_5_5', 'δοκιμη 6 0.5_5_5']

navier_stokes_file_name = 'navierStokesValues.txt'

navier_stokes_datasets = []
time = []  # Initialize the time array

# Read the Navier-Stokes values from the specified directories
for test_dir in test_dirs:
    navier_stokes = []
    file_path = os.path.join(base_path, test_dir, navier_stokes_file_name)
    if os.path.exists(file_path):  # Ensure the file exists
        with open(file_path, "r") as f:
            for line in f:
                t, val = line.split()
                time.append(float(t))  # Populate time array
                navier_stokes.append(float(val))
        navier_stokes_datasets.append(navier_stokes)

# Ensure the `time` array is consistent in size with `navier_stokes`
time = list(set(time))  # In case time has duplicates, ensure unique values
time.sort()  # Ensure time is in order

# Directory to save the plots
save_dir = r'C:\Users\mario\Desktop\Saved_Plots_NavierStokes'
os.makedirs(save_dir, exist_ok=True)  # Create the directory if it doesn't exist

# Color, marker, linestyle, and line width customization
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']
markers = ['o', '^', 's', 'd', 'x', '*']  # Different markers for each line
linestyles = ['-', '--', '-.', ':', '-', '--']  # Different linestyles for each line
linewidths = [2, 2, 2, 2, 2, 2]  # Line width for each plot

# --- Plot each dataset separately and save them ---
for i, navier_stokes in enumerate(navier_stokes_datasets):
    plt.figure(figsize=(10, 6))  # Create a new figure for each dataset

    # Plot the individual dataset
    plt.plot(time, navier_stokes, label=f'Test {i+1}: δοκιμή {i+1}', 
             color=colors[i], marker=markers[i], linestyle=linestyles[i], 
             markersize=8, linewidth=linewidths[i])

    # Title and subtitle for each plot
    plt.title(f'Navier-Stokes Parameters of Test {i+1} Over Time', fontsize=18, weight='bold')

    # Axis labels
    plt.xlabel('Time (s)', fontsize=14)
    plt.ylabel('Navier-Stokes Variable (units)', fontsize=14)

    # Legend for the individual plot
    plt.legend(fontsize=12, loc='upper left', bbox_to_anchor=(1, 1), title="Test Case", title_fontsize=13)

    # Add a subtle grid
    plt.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)

    # Use tight layout for each plot
    plt.tight_layout()

    # Save the individual plot as a .jpg file
    save_path = os.path.join(save_dir, f'navier_stokes_test_{i+1}.jpg')
    plt.savefig(save_path, format='jpg')  # Save as jpg

    # Display the individual plot
    plt.show()

# --- Now plot all datasets together on a single plot and save it ---
plt.figure(figsize=(10, 6))  # Create a new figure for the combined plot

# Plot all datasets together
for i, navier_stokes in enumerate(navier_stokes_datasets):
    plt.plot(time, navier_stokes, label=f'Test {i+1}: δοκιμή {i+1}', 
             color=colors[i], marker=markers[i], linestyle=linestyles[i], 
             markersize=8, linewidth=linewidths[i])

# Title for the combined plot
plt.title('Navier-Stokes Parameters Over Time for All Tests', fontsize=18, weight='bold')

# Axis labels for the combined plot
plt.xlabel('Time (s)', fontsize=14)
plt.ylabel('Navier-Stokes Variable (units)', fontsize=14)

# Legend for the combined plot
plt.legend(fontsize=12, loc='upper left', bbox_to_anchor=(1, 1), title="Test Cases", title_fontsize=13)

# Add a grid for the combined plot
plt.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)

# Use tight layout for the combined plot
plt.tight_layout()

# Save the combined plot as a .jpg file
combined_save_path = os.path.join(save_dir, 'navier_stokes_all_tests_combined.jpg')
plt.savefig(combined_save_path, format='jpg')  # Save as jpg

# Display the combined plot
plt.show()
