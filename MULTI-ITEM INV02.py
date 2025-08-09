import matplotlib.pyplot as plt

def simular_inventario(botellas_producto, inventario_inicial, punto_de_reorden, Cantidad_reorden, lead_time, pronostico_demanda):
    inventario = inventario_inicial
    orders = []
    daily_inventory_levels = []

    print(f"\n===== Simulación para: {botellas_producto} =====")
    for day in range(len(pronostico_demanda)):
        demand = pronostico_demanda[day]
        inventario -= demand

        for order in orders[:]:
            order[0] -= 1
            if order [0] <= 0:
                inventario += order[1]
                orders.remove(order)

        if inventario <= punto_de_reorden and not any(order[1] == Cantidad_reorden for order in orders):
            orders.append([lead_time, Cantidad_reorden])

        daily_inventory_levels.append(inventario)

        print(f" Día {day + 1}:")
        print(f"  Demanda: {demand}")
        print(f"  Inventario: {inventario}")
        print(f"  Pedidos pendientes: {orders}")

    return daily_inventory_levels

productos = [
    {
        # ROL es punto de reorden#
        # Y ROQ es cantidad de pedido
        "nombre": "Producto PET",
        "inventario_inicial": 500,
        "rol": 50,
        "roq": 100,
        "lead_time": 2,
        "demanda": [200, 150, 100, 70, 10, 8, 7, 9]
    },
    {
        "nombre": "Producto PLASTICO DURO",
        "inventario_inicial": 80,
        "rol": 40,
        "roq": 150,
        "lead_time": 2,
        "demanda": [8, 10, 9, 12, 11, 7, 6, 8]
    },
    {
        "nombre": "Producto Vidrio",
        "inventario_inicial": 120,
        "rol": 60,
        "roq": 180,
        "lead_time": 4,
        "demanda": [14, 13, 12, 15, 14, 10, 9, 11]
    },
    {
        "nombre": "Producto Caguama",
        "inventario_inicial": 90,
        "rol": 45,
        "roq": 160,
        "lead_time": 3,
        "demanda": [9, 11, 10, 13, 9, 8, 7, 9]
    },
    {
        "nombre": "Producto Metal",
        "inventario_inicial": 70,
        "rol": 30,
        "roq": 140,
        "lead_time": 2,
        "demanda": [7, 6, 8, 9, 6, 5, 4, 7]
    }
]

for producto in productos:
    simular_inventario(
        producto["nombre"],
        producto["inventario_inicial"],
        producto["rol"],
        producto["roq"],
        producto["lead_time"],
        producto["demanda"]
    )

    plt.figure(figsize=(12, 6))

    for producto in productos:
        niveles = simular_inventario(
            producto["nombre"],
            producto["inventario_inicial"],
            producto["rol"],
            producto["roq"],
            producto["lead_time"],
            producto["demanda"]
        )
        plt.plot(range(1, len(niveles) + 1), niveles, label=producto["nombre"])

    plt.title("Niveles de Inventario por Producto")
    plt.xlabel("Día")
    plt.ylabel("Inventario")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()