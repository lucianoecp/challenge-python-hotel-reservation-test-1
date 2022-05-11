import re 
import datetime

class Hotel:
    def __init__(self,
                 nome=None,
                 classe=None,
                 txNormal=None,
                 txFidelidade=None,
                 txFimDeSemanaN=None,
                 txFimDeSemanaF=None):
        
        self.nome               =   nome
        self.classe             =   classe
        self.txNormal           =   txNormal
        self.txFidelidade       =   txFidelidade
        self.txFimDeSemanaN     =   txFimDeSemanaN
        self.txFimDeSemanaF     =   txFimDeSemanaF
          
class Reserva:
    # Hoteis
    lakewood    =   Hotel("Lakewood", 3, 110.00, 80.00, 90.00, 80.00)
    bridgewood  =   Hotel("Bridgewood", 4, 160.00, 110.00, 60.00, 50.00)
    ridgewood   =   Hotel("Ridgewood", 5, 220.00, 100.00, 150.00, 40.00)   
    
    def __init__(self):
        self.datas  =   None
        self.tipo   =   None
        self.hotel  =   None
    
    
    
        
        
        