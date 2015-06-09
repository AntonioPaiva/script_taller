# -*- coding: cp1252 -*-
# 25/09/2015
# Ejemplo de wxPython 
# El Viaje del Navegante 

import wx

from con_bd import Connexion

class subclase_frame(wx.Frame):
    def __init__(self):

        # Llamamos al init (código del constructor) del wx.Frame del que 
        # heredamos.
		#Subclase del Frame
        wx.Frame.__init__(self, None, -1, 'Bienvenidos al Sistema ',
        pos=wx.Point(300, 400),size=wx.Size(800,850))

        # Id_usuario.
        self.etiquetaNombre = wx.StaticText(id=-1,label='Id_usuario',
        name='etiquetaId_usuario', parent=self,pos=wx.Point(16, 20),
        size=wx.Size(105, 60), style=0)

		#crea la grilla, caja de texto id_usuario
        self.textoIdusuario = wx.TextCtrl(id=-1, name='textoIdusuario',
        parent=self, pos=wx.Point(105, 20), size=wx.Size(288, 21))
		
		 # Nombre. 
        self.etiquetaNombre = wx.StaticText(id=-1,label='Nombre',
        name='etiquetaNOmbre', parent=self,pos=wx.Point(16, 50),
        size=wx.Size(54, 13), style=0)

		#crea la grilla, caja de texto Nombre
        self.textoNombre = wx.TextCtrl(id=-1, name=' textoNombre',
        parent=self,pos=wx.Point(105, 50), size=wx.Size(288, 21))

        # Apellidos .
        self.etiquetaApellidos = wx.StaticText(id=-1,label='Apellidos',
        name='etiquetaApellidos', parent=self,pos=wx.Point(16, 80), 
        size=wx.Size(54, 13), style=0)
		
		#crea la grilla, caja de texto
        #self.textoApe = wx.TextCtrl(id=-1, name='textoApe', parent=self, pos=wx.Point(105, 80), size=wx.Size(288, 21))

        self.textoApellidos = wx.TextCtrl(id=-1, name='textoApe', 
        parent=self, pos=wx.Point(105, 80), size=wx.Size(288, 21))

        # Nro Cedula.
        self.etiquetaCI = wx.StaticText(id=-1,label='Nro C.I.',
        name='etiquetaCI', parent=self,pos=wx.Point(16, 110),
        size=wx.Size(54, 13), style=0)

		#crea la grilla, caja de texto
        self.textoCedula = wx.TextCtrl(id=-1, name='textoNIF',parent=self,
        pos=wx.Point(105, 110), size=wx.Size(288, 21))

        # Dirección.
        self.etiquetaDireccion = wx.StaticText(id=-1,label='Dirección',
        name='etiquetaDireccion', parent=self,pos=wx.Point(16, 140),
        size=wx.Size(54, 13), style=0)

		#crea la grilla, caja de texto
        self.textoDireccion = wx.TextCtrl(id=-1, name='textoDireccion',
        parent=self,pos=wx.Point(105, 140), size=wx.Size(288, 21))

        #Ciudad.
        self.etiquetaCiudad = wx.StaticText(id=-1,label='Ciudad',
        name='etiquetaPais', parent=self,pos=wx.Point(16, 170),
        size=wx.Size(54, 13), style=0)

		#crea la grilla, caja de texto, ciudad
        self.textoCiudad = wx.TextCtrl(id=-1, name='textoPais',
        parent=self,pos=wx.Point(105, 170), size=wx.Size(288, 21))

        # Correo electrónico.        
        self.etiquetaEmail = wx.StaticText(id=-1,label='e-mail',
        name='etiquetaEmail', parent=self,pos=wx.Point(16, 200),
        size=wx.Size(54, 13), style=0)

		#crea la grilla, caja de texto, correo electronico
        self.textoEmail= wx.TextCtrl(id=-1, name='textoEmail',
        parent=self,pos=wx.Point(105, 200), size=wx.Size(288, 21))

        # Teléfono.
        self.etiquetaTelefono = wx.StaticText(id=-1,label='Teléfono',
        name='etiquetaTelefono', parent=self,pos=wx.Point(16, 230),
        size=wx.Size(54, 13), style=0)

		#crea la grilla, caja de texto
        self.textoTelefono = wx.TextCtrl(id=-1, name='textoTelefono',
        parent=self,pos=wx.Point(105, 230), size=wx.Size(288, 21))



        # Creamos un widget wx.Button, 3 widget wx.StaticText y 
        # 3 widget wx.TextCtrl.
        
        # Botón de salida de la aplicación.
        self.boton = wx.Button(self, id=-1,label="Salir",
        pos=wx.Point(296,310),size=wx.Size(75,23))

        # Creamos los manejadores de eventos, ligando los eventos a
        # los métodos que tendrán el código asociado.
        self.boton.Bind(wx.EVT_BUTTON, self.OnBotonSalir)
        self.Bind(wx.EVT_CLOSE, self.OnSalir)

	    # Botón de Insertar en la base de datos de la aplicación.
        self.botonInsertar = wx.Button(self, id=-1,label="Insertar",
        pos=wx.Point(200,310),size=wx.Size(75,23))
        self.botonInsertar.Bind(wx.EVT_BUTTON, self.insertar)

        # Creamos los manejadores de eventos, ligando los eventos a
        # los métodos que tendrán el código asociado.
        self.boton.Bind(wx.EVT_BUTTON, self.OnBotonSalir)
        self.Bind(wx.EVT_CLOSE, self.OnSalir)
        
        #boton menu principal 
        self.boton_menu_principal = wx.Button(self, id=-1,label="Menu Principal",
        pos=wx.Point(390,310),size=wx.Size(115,23))
        # Creamos los manejadores de eventos, ligando los eventos a
        # los métodos que tendrán el código asociado.
        #self.boton_menu_principal.Bind(wx.EVT_BUTTON, self.menu_principal)
          
    # Definimos los métodos que contienen el código que se ejecutará
    # cuando sean llamados a petición de los eventos definidos anteriormente.
    def OnBotonSalir(self, event):
        self.Close(True)

    def OnBotonSalir(self, event):
        self.Close(True)

    def OnSalir(self, event):
        # Destruimos el widget.
        self.Destroy()
        
    def insertar(self, event): 



def main():
		
	# Creamos una aplicación simple wx.
	aplicacion = wx.PySimpleApp()

	# Creamos el objeto frame, fruto de la instanciación de la clase 
	# subclase_frame.
	frame = subclase_frame()

	# Mostramos la instanciación de la clase subclase_frame.
	frame.Show()
	# Lanzamos el MainLoop, para escuchar peticiones de eventos.
	aplicacion.MainLoop()


if __name__ == '__main__':
	main()
#	main1()


