ticket_count = int(input("Введите количество билетов: "))
total_cost = 0
for i in range(ticket_count):
    age = int(input(f"Введите возраст посетителя {i+1}-го билета: "))
    if age < 18:
        ticket_price = 0
    elif age < 25:
        ticket_price = 990
    else:
        ticket_price = 1390
    total_cost += ticket_price

if ticket_count > 3:
    discount = 0.1 * total_cost
    total_cost -= discount

print(f"Сумма к оплате: {total_cost} руб.")
