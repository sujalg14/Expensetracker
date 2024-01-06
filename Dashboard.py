import customtkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from Backend import*


def createDashboardFrame(root):
    loadData()
    home_frame = customtkinter.CTkFrame(root, corner_radius=0, fg_color="transparent")
    home_frame.grid_columnconfigure(0, weight=1)
    home_frame.grid_columnconfigure(1, weight=1)
    home_frame.grid_columnconfigure(2, weight=1)
    home_frame.grid_columnconfigure(3, weight=1)
    home_frame.grid_rowconfigure(0, weight=1)
    home_frame.grid_rowconfigure(1, weight=1)
    home_frame.grid_rowconfigure(2, weight=1)
    home_frame.grid_rowconfigure(3, weight=1)
    home_frame.grid_rowconfigure(4, weight=1)
    home_frame.grid_rowconfigure(5, weight=1)
    home_frame.grid_rowconfigure(6, weight=1)
    home_frame.grid_rowconfigure(7, weight=1)
    home_frame.grid_rowconfigure(8, weight=1)
    # fonts

    # balance label
    font_balance = customtkinter.CTkFont(family="Poppins Regular", size=15)
    label_balance = customtkinter.CTkLabel(master=home_frame, text="Balance", anchor="w", font=font_balance)
    label_balance.grid(row=0, column=0, padx=20, sticky="nw")

    # total balance
    if round(AllTransactions[len(AllTransactions) - 1].availableBalance) < 0:
        color = "red"
    else:
        color = "green"
    font_totalBalance = customtkinter.CTkFont(family="Poppins Bold", size=25)
    label_totalBalance = customtkinter.CTkLabel(master=home_frame, text="Rs." + str(f"{round(AllTransactions[len(AllTransactions) - 1].availableBalance):,}"
        ), text_color=color,
                                                font=font_totalBalance)
    label_totalBalance.grid(row=0, column=0, padx=20, pady=20, sticky="nw")

    # barchart
    canvas = FigureCanvasTkAgg(drawBarChart(), master=home_frame)
    canvas.draw()
    canvas.get_tk_widget().grid(row=2, column=0, columnspan=1, padx=20, sticky="nw")

    # loan label
    font_loan = customtkinter.CTkFont(family="Poppins Bold", size=20)
    label_loan = customtkinter.CTkLabel(master=home_frame, text="Loan", anchor="w", font=font_loan)
    label_loan.grid(row=3, column=0, padx=20, sticky="nw")

    # loan to be paid label
    font_tobePaid = customtkinter.CTkFont(family="Poppins Regular", size=15)
    label_tobePaid = customtkinter.CTkLabel(master=home_frame, text="To Be Payed", anchor="w", font=font_tobePaid)
    label_tobePaid.grid(row=4, column=0, padx=20, sticky="nw")

    # total loabn
    font_totalLoan = customtkinter.CTkFont(family="Poppins Bold", size=20)
    label_totalLoan = customtkinter.CTkLabel(master=home_frame, text="Rs." + str(f"{totalLoanToBePaid():,}"),
                                             font=font_totalLoan)
    label_totalLoan.grid(row=4, column=0, padx=20, pady=20, sticky="nw")

    # loan to be received label
    font_tobePaid = customtkinter.CTkFont(family="Poppins Regular", size=15)
    label_tobePaid = customtkinter.CTkLabel(master=home_frame, text="To Recieve", anchor="w", font=font_tobePaid)
    label_tobePaid.grid(row=4, column=0, padx=200, sticky="nw")

    # total loabn
    font_totalLoan = customtkinter.CTkFont(family="Poppins Bold", size=20)
    label_totalLoan = customtkinter.CTkLabel(master=home_frame, text="Rs." + str(f"{totalLoanToRecieve():,}"),
                                             font=font_totalLoan)
    label_totalLoan.grid(row=4, column=0, padx=200, pady=20, sticky="nw")

    # Monthly expense limit
    font_expenseLimit = customtkinter.CTkFont(family="Poppins Regular", size=15)
    label_expenseLimit = customtkinter.CTkLabel(master=home_frame, text="Monthly Expense Limit:", anchor="nw",
                                                font=font_expenseLimit)
    label_expenseLimit.grid(row=2, column=1, sticky="nw")

    # mothly expense limit amount label
    font_expenseLimitAmount = customtkinter.CTkFont(family="Poppins Bold", size=20)
    label_expenseLimitAmount = customtkinter.CTkLabel(master=home_frame, text="Rs." + str(f"{getMonthlyExpenseLimit():,}"),
                                                      anchor="w", font=font_expenseLimitAmount)
    label_expenseLimitAmount.grid(row=2, column=1, pady=20, sticky="nw")

    # This month's expenses
    font_thisMonthLimit = customtkinter.CTkFont(family="Poppins Regular", size=15)
    label_thisMonthLimit = customtkinter.CTkLabel(master=home_frame, text="This Month's Expenses:", anchor="nw",
                                                  font=font_thisMonthLimit)
    label_thisMonthLimit.grid(row=2, column=1, pady=60, sticky="nw")

    # This month's expenses
    font_thisMonthLimitAmount = customtkinter.CTkFont(family="Poppins Bold", size=20)
    if (currentMonthExpenses() > getMonthlyExpenseLimit()):
        color = "red"
    else:
        color = "green"
    label_thisMonthLimitAmoun = customtkinter.CTkLabel(master=home_frame, text_color=color,
                                                       text="Rs." + str(f"{currentMonthExpenses():,}"), anchor="w",
                                                       font=font_thisMonthLimitAmount)
    label_thisMonthLimitAmoun.grid(row=2, column=1, pady=80, sticky="nw")

    # Cash flow for december label
    font_cashflowLabel = customtkinter.CTkFont(family="Poppins Regular", size=15)
    label_cashflowLabe = customtkinter.CTkLabel(master=home_frame, text="Cash flow for " + get_current_month_name(),
                                                anchor="w",
                                                font=font_cashflowLabel)
    label_cashflowLabe.grid(row=4, column=1, sticky="nw")

    # Earned label
    font_earnedLabel = customtkinter.CTkFont(family="Poppins Regular", size=10)
    label_earnedLabel = customtkinter.CTkLabel(master=home_frame, text="EARNED", anchor="w", font=font_earnedLabel)
    label_earnedLabel.grid(row=4, column=1, pady=20, sticky="nw")

    # Earned amount label
    font_amountEarned = customtkinter.CTkFont(family="Poppins Bold", size=10)
    label_amountEarned = customtkinter.CTkLabel(master=home_frame, text="Rs." + str(f"{currentMonthEarning():,}"), anchor="w",
                                                font=font_amountEarned)
    label_amountEarned.grid(row=4, column=1, padx=150, pady=20, sticky="nw")

    # progess bar
    progressbar = customtkinter.CTkProgressBar(master=home_frame)
    progressbar.set(get_percentage(currentMonthEarning(), getMonthlyExpenseLimit()))
    progressbar.grid(row=4, column=1, pady=40, sticky="nw")

    # SPENT label
    font_spent_label = customtkinter.CTkFont(family="Poppins Regular", size=10)
    label_spent_Label = customtkinter.CTkLabel(master=home_frame, text="SPENT", anchor="w", font=font_spent_label)
    label_spent_Label.grid(row=4, column=1, pady=60, sticky="nw")

    # SPENT amount label
    font_spentAmount = customtkinter.CTkFont(family="Poppins Bold", size=10)
    label_spentAmount = customtkinter.CTkLabel(master=home_frame, text="Rs." + str(f"{currentMonthExpenses():,}"), anchor="w",
                                               font=font_spentAmount)
    label_spentAmount.grid(row=4, column=1, padx=150, pady=60, sticky="nw")

    # progess bar
    progressbar = customtkinter.CTkProgressBar(master=home_frame)
    progressbar.set(get_percentage(currentMonthExpenses(), getMonthlyExpenseLimit()))
    progressbar.grid(row=4, column=1, pady=80, sticky="nw")

    # Remaining cashflow amount label
    font_remainingAmount = customtkinter.CTkFont(family="Poppins Bold", size=20)
    if (currentMonthEarning() - currentMonthExpenses() < 0):
        color = "red"
    else:
        color = "green"
    label_remainingAmount = customtkinter.CTkLabel(master=home_frame, text_color=color,
                                                   text="Rs." + str(f"{currentMonthEarning() - currentMonthExpenses():,}"),
                                                   anchor="w", font=font_remainingAmount)
    label_remainingAmount.grid(row=4, column=1, padx=210, pady=45, sticky="nw")

    # Remaining label
    font_remainingLabel = customtkinter.CTkFont(family="Poppins Regular", size=10)
    label_remaining = customtkinter.CTkLabel(master=home_frame, text="REMAINING", anchor="w", font=font_remainingLabel)
    label_remaining.grid(row=4, column=1, pady=70, padx=210, sticky="nw")

    return home_frame
