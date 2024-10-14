import pandas as pd
from tkinter import Tk, Menu, messagebox

class Estudiantes:
    def __init__(self, archivo):
        self.data = pd.read_excel(archivo)

    def mostrar_completo(self):
        print(self.data)

    def mostrar_nombres(self):
        print(self.data["nombreApellido"])

    def mostrar_cantidad_hermanos(self):
        print(self.data["catHermanos"].sum())

    def mostrar_toda(self):
        print(self.data["edad"])

    def mostrar_mayores_de_18(self):
        mayores = self.data.query("edad >= 18")
        print(mayores)
        print("El total de mayores es:", len(mayores))

    def mostrar_media(self):
        media = self.data["edad"].mean()
        return media

    def mostrar_mediana(self):
        mediana = self.data["edad"].median()
        return mediana

    def mostrar_moda(self):
        moda = self.data["edad"].mode()
        return moda[0]


class Aplicacion:
    def __init__(self, master, estudiantes):
        self.master = master
        self.estudiantes = estudiantes
        self.master.title("Excel Hnos")
        self.master.geometry("800x600")
        self.crear_menu()

    def crear_menu(self):
        
        menu_bar = Menu(self.master)

        # Primer menú
        menu_excel = Menu(menu_bar, tearoff=0)
        menu_excel.add_command(label="Completo", command=self.estudiantes.mostrar_completo)
        menu_excel.add_command(label="Nombres", command=self.estudiantes.mostrar_nombres)
        menu_excel.add_command(label="Cantidad de Hermanos", command=self.estudiantes.mostrar_cantidad_hermanos)
        menu_bar.add_cascade(label="Excel", menu=menu_excel)

        # Segundo menú
        menu_edades = Menu(menu_bar, tearoff=0)
        menu_edades.add_command(label="Toda", command=self.estudiantes.mostrar_toda)
        menu_edades.add_command(label="18", command=self.estudiantes.mostrar_mayores_de_18)
        menu_bar.add_cascade(label="Edades", menu=menu_edades)

        # Tercer menú
        menu_promedios = Menu(menu_bar, tearoff=0)
        menu_promedios.add_command(label="Media", command=self.mostrar_media)
        menu_promedios.add_command(label="Mediana", command=self.mostrar_mediana)
        menu_promedios.add_command(label="Moda", command=self.mostrar_moda)
        menu_bar.add_cascade(label="Promedios", menu=menu_promedios)

        # Configurar la barra de menú
        self.master.config(menu=menu_bar)

    def mostrar_media(self):
        media = self.estudiantes.mostrar_media()
        messagebox.showinfo("Media", f"Media aritmética: {media}")

    def mostrar_mediana(self):
        mediana = self.estudiantes.mostrar_mediana()
        messagebox.showinfo("Mediana", f"Mediana: {mediana}")

    def mostrar_moda(self):
        moda = self.estudiantes.mostrar_moda()
        messagebox.showinfo("Moda", f"Moda: {moda}")


if __name__ == "__main__":
    nombre_archivo = "/home/quintob/Benja Gómez/pueba.xls"
    estudiantes = Estudiantes(nombre_archivo)
    
    ventana = Tk()
    app = Aplicacion(ventana, estudiantes)
    ventana.mainloop()
