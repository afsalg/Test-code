# Build a menu
title = "menu" .upper()
coffee = "Koffie"
coffeeprice = "€1"
muffin = "Muffin"
muffinprice = "€2" # € alt+0128
cheesecake = "Cheescake"
cheesecakeprice = "€4"

# print (title.center(20, "="))
# print ("Coffee".ljust(16, ".") + "$1".rjust(4))
# print ("Muffin".ljust(16, ".") + "$2".rjust(4))
# print ("Cheesecake".ljust(16, ".") + "$4".rjust(4))
# print ("")

print ("\n" + title.center(22, "="), end=" * ")
print (title.center(22, "="))
print (coffee.ljust(16, "_") + coffeeprice.rjust(6), end=" * ")
print (coffee.ljust(16, "_") + coffeeprice.rjust(6))
print (muffin.ljust(16, "_") + muffinprice.rjust(6), end=" * ")
print (muffin.ljust(16, "_") + muffinprice.rjust(6))
print (cheesecake.ljust(16, "_") + cheesecakeprice.rjust(6), end=" * ")
print (cheesecake.ljust(16, "_") + cheesecakeprice.rjust(6))