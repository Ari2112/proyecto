class Persistencia:
    listado_Articulos = []
    
    @classmethod
    def agregar_articulo(self,objeto):
        self.listado_Articulos.append(objeto)
    
    @classmethod    
    def control_articulo(self):
        return self.listado_Articulos
    @classmethod
    def crear_bodegas(self):
        pass
    @classmethod
    def perfil_distribuidores(self):
        pass