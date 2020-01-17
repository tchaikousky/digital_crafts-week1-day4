power_rangers = ["Jason", "Trini", "Zach", "Billy", "Kim", "Tommy"]
who_to_remove = input("Who do you want to remover? ")

#print(power_rangers)

if(who_to_remove in power_rangers):
    power_rangers.remove(who_to_remove)
    print(power_rangers)
else:
    print("%s isn't part of the group." % who_to_remove)
