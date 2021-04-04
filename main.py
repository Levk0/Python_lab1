class ITCLUSTER:
    city = None
    numberOfMembers = None
    ceo = None
    officeAddress = None
    country = None
    yearOfFoundation = None

    def __init__(self, city=None, numberOfMembers=None, ceo=None, officeAddress=None, country=None,
                 yearOfFoundation=None):
        self.city = city
        self.numberOfMembers = numberOfMembers
        self.ceo = ceo
        self.officeAddress = officeAddress
        self.country = country
        self.yearOfFoundation = yearOfFoundation

    def __del__(self):
        return

    def __str__(self):
        return f"City: {self.city}\n" \
               f"Number of members: {self.numberOfMembers}\n" \
               f"CEO: {self.ceo}\n" \
               f"Office address: {self.officeAddress}\n" \
               f"Country: {self.country}\n" \
               f"Year of foundation: {self.yearOfFoundation}"


def main():
    itcluster_1 = ITCLUSTER("Lviv", "81 companies", "Stepan Veselovskiy", "Vesnyana 4 street, Lviv", "Ukraine", "2012")

    itcluster_2 = ITCLUSTER("Lviv", "81 companies", "Stepan Veselovskiy")

    itcluster_3 = ITCLUSTER()

    print("_________________________________________")
    print(itcluster_1)
    print("_________________________________________")
    print(itcluster_2)
    print("_________________________________________")
    print(itcluster_3)
    print("_________________________________________")


if __name__ == "__main__":
    main()
