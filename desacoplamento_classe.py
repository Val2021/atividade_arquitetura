import string
import random

class Vehicle:
    def __init__(self,brand:str,catalogue_price:int,tax_percentage:float, is_eletric=False) -> None:
        self.brand = brand
        self.catalogue_price = catalogue_price
        self.vehicle_id=None
        self.license_plate = None
        self.is_eletric = is_eletric
        self.tax_percentage=tax_percentage



class VehicleRegistry:

    def generate_vehicle_id(self, length):
        return ''.join(random.choices(string.ascii_uppercase, k=length))

    def generate_vehicle_license(self, id):
        first_section = id[:2]
        second_section = ''.join(random.choices(string.digits, k=2))
        third_section = ''.join(random.choices(string.ascii_uppercase, k=2))
        return f"{first_section}-{second_section}-{third_section}"




class Application:

    VEHICLES=[
     Vehicle(brand='Tesla Model 3',tax_percentage=0.02,catalogue_price=445000,is_eletric=True),
     Vehicle(brand='Chevrolet Bold',tax_percentage=0.02,catalogue_price=317000,is_eletric=True),
     Vehicle(brand='BMW i3',tax_percentage=0.05,catalogue_price=319950,is_eletric=False),
     Vehicle(brand='Honda Civic LX',tax_percentage=0.05,catalogue_price=127900,is_eletric=False),
    ]

    def register_vehicle(self, brand: string):
        registry = VehicleRegistry()
        vehicle = None
        for v in  self.VEHICLES:
            if v.brand == brand:
               vehicle = v
        if vehicle:
            # gera um id com 12 caracteres
            vehicle.vehicle_id = registry.generate_vehicle_id(12)

            # gera a placa de baseado no id do veículo
            vehicle.license_plate = registry.generate_vehicle_license(vehicle.vehicle_id)



            # calcula a valor a ser pago
            payable_tax = vehicle.tax_percentage * vehicle.catalogue_price


            print(f'Marca: {brand}')
            print(f'ID: {vehicle.vehicle_id}')
            print(f'Placa: {vehicle.license_plate}')
            print(f'Imposto a ser pago: {payable_tax}')
        else:
            print("Não existe veículo com essa marca")


app = Application()
app.register_vehicle('Tesla Model 3')
