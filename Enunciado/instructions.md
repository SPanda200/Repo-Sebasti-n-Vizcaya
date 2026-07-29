## Introducción

Eres el manager del ultimo Blockbuster del mundo. Todos los días llegan clientes a arrendar nuevas peliculas. Decides crear un crear un programa que haga tu trabajo por ti, para dedicarte a ver peliculas todo el día en tu oficina. 

## Objetivo


Debes crear una clase Cliente. Debe tener las siguientes funciones:

`__init__`, que tome los siguientes parametros:

`nombre`, un string.

`preferencia`, una lista que contiene el orden de preferencia de generos de pelicula.

`VIP`, un booleano que determina si es cliente VIP o no.

`demanda`, un int que representa cuantas peliculas quiere arrendar.

También debes crear la clase Blockbuster, que debe tener las variables nombre, stock, capacidad, profit, clientes_atendidos, fila, y orden_atencion. Debe tener las siguientes funciones:

`__init__`, que tome los siguientes parametros:

`nombre`, un string.

`stock`, una lista que contiene todas las peliculas en stock. Las peliculas vienen en el siguiente formato: `[["Titulo1", "Genero", "Valor"],["Titulo2", "Genero", "Valor"]...["TituloN", "Genero", "Valor"]]`. Por ejemplo, `[["Matrix", "Acción", 1500],["Minions", "Comedia", 2000]]`.

`capacidad`, un int que determina cuantos clientes puedes atender en un dia. 

Ademas, debes tener los ints `profit`, `peliculas_arrendadas`, y `clientes_atendidos`, que comienzan en 0, y las listas vacias `fila` y `orden_atencion`.

`recibir_cliente(cliente)`, que toma como parametro un objeto Cliente. Si es que queda capacidad en la tienda, debes agregarlo a la fila, e imprimir `"{nombre_cliente} entra al Blockbuster {nombre_tienda}"`. En caso contrario, debes imprimir `"{nombre_cliente} se va llorando al no caber adentro de la tienda"`

`ordenar_prioridad`, no toma parametros. Debe armar la lista `orden_atencion` basado en la fila que se armó. Primero debes atender a los clientes VIP según su orden de llegada, y despues a los otros según su orden de llegada. 

`generar_venta(cliente)`, toma como parametro un objeto Cliente. Debes buscar peliculas para el cliente de tu stock que cumpla sus preferencias hasta satisfacer su demanda. En caso de que no tengas ninguna del genero que mas le gusta, debes revisar del siguiente genero en su lista. Asume que siempre va a haber al menos una pelicula que le guste al cliente. Como queremos maximizar las ganancias, si hay mas de una pelicula en el genero preferido, primero debes arrendar la mas cara. Cuando arriendes una pelicula, debes eliminarla del stock, añadir su precio al profit, aumentar el numero de peliculas arrendadas, e imprimir `"{nombre_cliente} arrienda {nombre_pelicula} por {precio}"`. Al finalizar la transacción, aumenta el numero de clientes atendidos e imprime `"{nombre_cliente} arrendó {numero_peliculas} pelicula(s), gastando {precio_total}"`

`trabajar(clientes)`, toma como parametro una lista de objetos Cliente. Debe simular un dia completo de trabajo, primero imprimiendo `"---Se abre el Blockbuster {nombre}---"`; luego recibiendo a todos los clientes de la lista, y atendiendolos en orden hasta que todos hayan sido atendidos. Para finalizar el día, debes imprimir `"---Cerrando la caja---"`, y despues `"Se atendieron {n_clientes} clientes, se arrendaron {n_peliculas} peliculas, y ganamos ${profit}"`, finalmente debes imprimir `"---Se cierra el Blockbuster {nombre}---"`

## Ejemplo

Acá se debe poner un ejemplo de input y el output esperado para dicho input, junto con una breve explicación de por qué se llega a ese output.

#### Input
```py
stock = [["Matrix", "Accion", 1500], ["Terminator", "Accion", 2000], ["Minions", "Comedia", 1000], ["El Padrino", "Drama", 2500]]

tienda = Blockbuster("Github", stock, 3)

clientes = [Cliente("Juan", ["Accion", "Comedia"], False, 2), Cliente("Maria", ["Accion"], True, 1), Cliente("Pedro", ["Comedia", "Drama"], False, 1), Cliente("Juana", ["Drama"], True, 3)]

tienda.trabajar(clientes)

```

#### Output
```
---Se abre el Blockbuster Github---
Juan entra al Blockbuster Github
Maria entra al Blockbuster Github
Pedro entra al Blockbuster Github
Juana se va llorando al no caber adentro de la tienda
Maria arrienda Terminator por 2000
Maria arrendó 1 pelicula(s), gastando 2000
Juan arrienda Matrix por 1500
Juan arrienda Minions por 1000
Juan arrendó 2 pelicula(s), gastando 2500
Pedro arrienda El Padrino por 2500
Pedro arrendó 1 pelicula(s), gastando 2500
---Cerrando la caja---
Se atendieron 3 clientes, se arrendaron 4 peliculas, y ganamos $7000
---Se cierra el Blockbuster Github---

```
**Explicación:** 

Los primeros tres clientes entran, pero Juana no debido a la capacidad de la tienda. Ya que Maria es VIP, se le atiende primero, y despues Juan y Pedro por orden de llegada. Maria prefiere las peliculas de accion, y como hay dos opciones, toma la mas cara. Despues se atiende a Juan, que quiere dos peliculas. Primero arrienda Matrix debido a su preferencia, pero no quedan mas peliculas de Acción, por lo que pasa a su siguiente preferencia, la comedia, y arrienda Minions. Finalmente, se atiende a Pedro, y se lleva la pelicula que el prefiere. Como ya no quedan mas clientes por atender, se cierra la caja y la tienda.
