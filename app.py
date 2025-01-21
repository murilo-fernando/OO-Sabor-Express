from modelos.restaurante import Restaurante
restaurante_praca= Restaurante('Praça','Gourmet')
restaurante_mexicano= Restaurante('Mexican food','Mexicana')
restaurante_japones= Restaurante('japa','Japonesa')
restaurante_pizza= Restaurante('Pizza Express','Italiana')

restaurante_praca.receber_avaliacao('Murilo',10)
restaurante_praca.receber_avaliacao('MURILO',8)
restaurante_praca.receber_avaliacao('Murilo-Fernando',7)

restaurante_japones.alternar_estado()

def main():
    Restaurante.listar_restaurantes()


if __name__== '__main__':
    main()