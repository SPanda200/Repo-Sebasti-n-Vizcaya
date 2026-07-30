class Cliente:

  def __init__(self, nombre, preferencia, VIP, demanda):
    self.nombre = nombre
    self.preferencia = preferencia
    self.VIP = VIP
    self.demanda = demanda

class Blockbuster:

  def __init__(self, nombre, stock, capacidad):
        self.nombre = nombre
        self.stock = stock
        self.capacidad = capacidad
        self.profit = 0
        self.peliculas_arrendadas = 0
        self.clientes_atendidos = 0
        self.fila = []
        self.orden_atencion = []

  def recibir_cliente(self, cliente):
        if len(self.fila) < self.capacidad:
            self.fila.append(cliente)
            print(cliente.nombre + " entra al Blockbuster " + self.nombre)
        else:
            print(cliente.nombre + " se va llorando al no caber adentro de la tienda")

  def ordenar_prioridad(self):
    vip = []
    normal = []
    for cliente in self.fila:
      if cliente.VIP:
        vip.append(cliente)
      else:
        normal.append(cliente)
    self.orden_atencion = vip + normal

  def generar_venta(self, cliente):
    arrendadas = 0
    ganancia = 0
    while arrendadas < cliente.demanda:
      posibles = []
      genero = 0
      while True:
        for i in self.stock:
          if i[1] == cliente.preferencia[genero]:
            posibles.append(i)
        if len(posibles) > 0:
          break
        else:
          genero += 1
      target = posibles[0]
      for i in posibles:
        if i[2] > target[2]:
          target = i
      self.stock.remove(target)
      ganancia += target[2]
      arrendadas += 1
      self.peliculas_arrendadas += 1
      print(cliente.nombre + " arrienda " + target[0] + " por " + str(target[2]))
    self.profit += ganancia
    self.clientes_atendidos += 1
    print(cliente.nombre + " arrendó " + str(arrendadas) + " pelicula(s), gastando " + str(ganancia))

  def trabajar(self, clientes):
    print("---Se abre el Blockbuster " + self.nombre + "---")
    for i in clientes:
      self.recibir_cliente(i)
    self.ordenar_prioridad()
    for i in self.orden_atencion:
      self.generar_venta(i)
    print("---Cerrando la caja---")
    print("Se atendieron "+str(self.clientes_atendidos)+" clientes, se arrendaron "+str(self.peliculas_arrendadas)+" peliculas, y ganamos $"+str(self.profit))
    print("---Se cierra el Blockbuster "+self.nombre+"---")
      
        
      
