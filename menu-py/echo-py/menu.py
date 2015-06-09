# -*- coding: cp1252 -*-
# 25/09/2015
# Ejemplo de wxPython 
# El Viaje del Navegante 

import wx

class login(wx.Frame):
    def __init__(self):

        # Llamamos al init (código del constructor) del wx.Frame del que 
        # heredamos.
		#Subclase del Frame
        wx.Frame.__init__(self, None, -1, 'Bienvenidos al Sistema',
        pos=wx.Point(300, 400),size=wx.Size(800,850))
        
        self.mensaje_menu = wx.StaticText(id=-1,label='MENU PRINCIPAL',
        name='mensaje', parent=self,pos=wx.Point(200, 90), size=wx.Size(300,1000), style=0)
        
        self.mensaje_menup = wx.StaticText(id=-1,label='MENU PRINCIPAL',name='mensaje', 
        parent=self,pos=wx.Point(200, 90), size=wx.Size(300,1000), style=0)
        
        self.mensaje_opcion = wx.StaticText(id=-1,label='ELIJA UNA OPCIÓN',name='mensaje',
        parent=self,pos=wx.Point(200, 110), size=wx.Size(300,1000), style=0)
        
        self.mensaje_opcionp = wx.StaticText(id=-1,label='ELIJA UNA OPCIÓN',name='mensaje',
        parent=self,pos=wx.Point(200, 110), size=wx.Size(300,1000), style=0)
        
        self.boton_ingresar = wx.Button(self, id=-1,label="MENU CLIENTES",
        pos=wx.Point(200, 150),size=wx.Size(120,55))
        
        self.boton_ingresar = wx.Button(self, id=-1,label="MENU EMPLEADOS",
        pos=wx.Point(200, 220),size=wx.Size(120,55))
        
        # Botón de salida de la aplicación.
        self.boton_ingresar = wx.Button(self, id=-1,label="SALIR",
        pos=wx.Point(200,290),size=wx.Size(120,55))
        self.boton_ingresar.Bind(wx.EVT_BUTTON, self.ingresar_menu)
               
    # Definimos los métodos que contienen el código que se ejecutará
    # cuando sean llamados a petición de los eventos definidos anteriormente.
    def ingresar_menu(self, event):
        admin = "admin"
        cont_reg = "12345"
        
        usuar = self.texto_usuario.GetValue()
        cont = self.texto_contrasenha.GetValue()
        
        if cont_reg == cont:
            print "Bienvenido al Sistema!"
        else:
            print "Valor incorrecto"

def main():
		
	# Creamos una aplicación simple wx.
	aplicacion = wx.PySimpleApp()

	# Creamos el objeto frame, fruto de la instanciación de la clase 
	# subclase_frame.
	frame = login()

	# Mostramos la instanciación de la clase subclase_frame.
	frame.Show()
	# Lanzamos el MainLoop, para escuchar peticiones de eventos.
	aplicacion.MainLoop()


if __name__ == '__main__':
	main()
#	main1()


