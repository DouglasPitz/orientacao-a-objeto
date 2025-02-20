from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça','Gourmet')
#restaurate_mexicano = Restaurante('Mexican Food','Mexicana')
#restaurante_japones = Restaurante('Japa','Japonesa')

restaurante_praca.receber_avaliacao('Guilherme', 10)
restaurante_praca.receber_avaliacao('Juliana', 8)
restaurante_praca.receber_avaliacao('Douglas', 5)

#restaurate_mexicano.alternar_estado()

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()