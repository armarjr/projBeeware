"""
Esse e um projeto de estudo de beeware com Toga
"""

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class ProjetoBeewarecomToga(toga.App):
    def startup(self):
        """
          criacao do box principal
        """
        main_box = toga.Box(style=Pack(direction=COLUMN))

        '''
            criar box direita, box meio  e box esquerda
        '''
        box_esquerda = toga.Box()
        
        box_meio = toga.Box()
        
        box_direita = toga.Box()

        
        '''
            criacao de boxes 
        '''
        box_nome = toga.Box(style=Pack(direction=ROW))
        box_idade= toga.Box(style=Pack(direction=ROW))
        box_sexo= toga.Box(style=Pack(direction=ROW))
        
        ''' 
            criacao dos widgets 
        '''
        label_nome= toga.Label(text="Nome")
        text_nome= toga.TextInput(style=Pack(flex=1))
        label_idade= toga.Label(text="Idade")
        text_idade= toga.TextInput(style=Pack(flex=1))
        label_sexo= toga.Label(text="Sexo")
        text_sexo= toga.Selection(items=[ "Masculino", "Feminino"] , style=Pack(flex=0))
        
        '''
            insersao dos widgets nos boxes
        '''
        box_nome.add(label_nome)
        box_nome.add(text_nome)
        box_idade.add(label_idade)
        box_idade.add(text_idade)
        box_sexo.add(label_sexo)
        box_sexo.add(text_sexo)
        
        '''
            adicionar os box com widgets no box da esquerda    
        '''
        box_esquerda.add(box_nome)
        box_esquerda.add(box_idade)
        box_esquerda.add(box_sexo)  
        
        '''
            criacao de botao
        '''
        botao_imprimir = toga.Button(text="Imprimir")
        
        '''
            adicao do botao no box a direita
        '''
        box_direita.add(botao_imprimir)
        

        
                
        '''
            insersao dos boxes na main_box
        '''
        
        main_box.add(box_direita)
        main_box.add(box_meio)
        main_box.add(box_esquerda)
        
        
        
        '''
            exibicao da main_box 
        '''
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()


def main():
    return ProjetoBeewarecomToga()
