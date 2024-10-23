import tkinter as tk
from tkinter import messagebox
#Made by ApexChicken on Github

# Function to clear input fields after calculation
def clear_fields():
    entry_client_name.delete(0, tk.END)
    entry_print_name.delete(0, tk.END)
    entry_date.delete(0, tk.END)
    entry_filament_cost.delete(0, tk.END)
    entry_filament_amt_bought.delete(0, tk.END)
    entry_filament_used.delete(0, tk.END)
    entry_print_time.delete(0, tk.END)
    entry_model_design_time.delete(0, tk.END)
    totalPriceLabel.config(text="Total Price: $0.00")

# Function to calculate the 3D print cost
def calculate_3d_print_cost():
    try:
        filamentCost = float(entry_filament_cost.get())
        filamentAmtBought = float(entry_filament_amt_bought.get())
        filamentUsed = float(entry_filament_used.get())
        printTime = float(entry_print_time.get())
        modelDesignTime = float(entry_model_design_time.get())

        # Static rates
        printRate = 2
        modelDesignRate = 3
        electricityCostPerHour = 0.25
        profitMargin = 0.15

        # Calculate costs
        materialCost = (filamentCost / filamentAmtBought) * filamentUsed
        printingCost = printRate * printTime
        designCost = modelDesignRate * modelDesignTime
        electricityCost = electricityCostPerHour * printTime
        totalCost = materialCost + printingCost + designCost + electricityCost
        totalCostWithProfit = totalCost * (1 + profitMargin)

        # Display the result in the label
        totalPriceLabel.config(text=f"Total Price: ${totalCostWithProfit:.2f}")

        # Save to a file
        clientName = entry_client_name.get()
        printName = entry_print_name.get()
        date = entry_date.get()

        file_name = f"{clientName}_Invoice_3dPrintCost.txt"
        with open(file_name, "w") as file:
            file.write(f"Name: {clientName}\n")
            file.write(f"Date: {date}\n")
            file.write(f"Print: {printName}\n")
            file.write(f"The total price for the 3D printed part is: ${totalCostWithProfit:.2f}\n")
            file.write("Payment is expected within 30 days of date. Thank you for working with us!")

        messagebox.showinfo("Saved", f"The result has been saved to {file_name}")
        
        # Clear input fields for next calculation
        clear_fields()

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers!")

# GUI setup
root = tk.Tk()
root.title("3D Print Cost Calculator")

# Client details
tk.Label(root, text="Client Name:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_client_name = tk.Entry(root)
entry_client_name.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Print Name:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_print_name = tk.Entry(root)
entry_print_name.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Date (mm/dd/yyyy):").grid(row=2, column=0, padx=10, pady=5, sticky="e")
entry_date = tk.Entry(root)
entry_date.grid(row=2, column=1, padx=10, pady=5)

# Cost inputs
tk.Label(root, text="Filament Cost ($):").grid(row=3, column=0, padx=10, pady=5, sticky="e")
entry_filament_cost = tk.Entry(root)
entry_filament_cost.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Filament Amount Bought (g):").grid(row=4, column=0, padx=10, pady=5, sticky="e")
entry_filament_amt_bought = tk.Entry(root)
entry_filament_amt_bought.grid(row=4, column=1, padx=10, pady=5)

tk.Label(root, text="Filament Used (g):").grid(row=5, column=0, padx=10, pady=5, sticky="e")
entry_filament_used = tk.Entry(root)
entry_filament_used.grid(row=5, column=1, padx=10, pady=5)

tk.Label(root, text="Print Time (hours):").grid(row=6, column=0, padx=10, pady=5, sticky="e")
entry_print_time = tk.Entry(root)
entry_print_time.grid(row=6, column=1, padx=10, pady=5)

tk.Label(root, text="Model Design Time (hours):").grid(row=7, column=0, padx=10, pady=5, sticky="e")
entry_model_design_time = tk.Entry(root)
entry_model_design_time.grid(row=7, column=1, padx=10, pady=5)

# Button to calculate
calculate_button = tk.Button(root, text="Calculate", command=calculate_3d_print_cost)
calculate_button.grid(row=8, columnspan=2, padx=10, pady=10)

# Label to display total price
totalPriceLabel = tk.Label(root, text="Total Price: $0.00", font=("Arial", 14))
totalPriceLabel.grid(row=9, columnspan=2, padx=10, pady=10)

root.mainloop()
