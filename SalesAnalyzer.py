class SalesAnalyzer:
    def __init__(self, sales):
        self.sales = sales

    def total_sales(self, department):
        def helper(index, count, total):
            if index == len(self.sales): 
                return [count, total]

            sale_data = self.sales[index].split(',')
            sale_department = sale_data[3]
            sale_total_price = float(sale_data[2])

            if sale_department == department:
                count += 1
                total += sale_total_price

            return helper(index + 1, count, total)

        result = helper(0, 0, 0.0)

        print(f"{result[0]} VENDAS")
        print(f"TOTAL = $ {result[1]:.2f}")

        return result