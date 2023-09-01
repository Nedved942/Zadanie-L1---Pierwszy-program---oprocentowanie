import csv

print("\n*** Pierwszy program - oprocentowanie ***\n")

initial_credit_value = float(input("Podaj początkową wartość kredytu: "))
interest_rate = float(input("Podaj oprocentowanie kredytu: "))
loan_installment = float(input("Podaj kwotę raty kredytu: "))

# # Przykładowe wartości zadania
# initial_credit_value = 12000
# interest_rate = 3
# loan_installment = 200

inflation_list = []
remain_credit_value_list = [initial_credit_value]

with open("Oprocentowanie1.csv", "r") as file:
    zmienna = csv.reader(file)
    for row in zmienna:
        inflation_list.append(float(row[0]))
        # print(len(inflation_list))  # końcowa liczba elementów to 24 równa liczbie miesięcy w ciągu 2 lat

# print(zmienna)  # jest to obiekt odczytanego pliku file


for element in range(24):
    remain_credit_value_list.append(
        (1 + ((inflation_list[element] + interest_rate) /
              (initial_credit_value / 10))) *
        remain_credit_value_list[element] - loan_installment
    )

    print(f"Twoja pozostała kwota kredytu to "
          f"{round(remain_credit_value_list[element + 1], 2)}, to "
          f"{round(remain_credit_value_list[element] - remain_credit_value_list[element + 1], 2)} "
          f"mniej niż w poprzednim miesiącu.")
