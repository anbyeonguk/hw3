def get_fixed_price(할인율, 할인가격):
    fixed_price =할인가격*100/(100-할인율)
    return fixed_price


할인율 = float(input("할인율은? "))
A할인가격 = float(input("A 상품의 할인 가격을 입력하세요: "))


B할인가격 = int(input("B 상품의 할인 가격을 입력하세요: "))


A_fixed_price = get_fixed_price(할인율, A할인가격)
B_fixed_price = get_fixed_price(할인율, B할인가격)

print("A 상품의 할인 전 가격:", A_fixed_price)
print("B 상품의 할인 전 가격:", B_fixed_price)