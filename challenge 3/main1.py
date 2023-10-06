def linearSearchProduct(productList, targetProduct):
 indices = []

 for index, product in enumerate(productList): 
   if product == targetProduct:
    indices.append(index)

 return indices

# Example usage:

products = ["apple", "orange", "apple", "lemon", "apple",
"papaya"]

target = "apple"

result = linearSearchProduct(products, target)
print(result)