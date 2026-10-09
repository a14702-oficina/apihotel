from flask_restful import Resource, reqparse
from models.hotel import HotelModel

hoteis = [
    {"hotel_id": "paraiso", "nome": "Hotel Paraiso", "estrelas": 4.8, "diaria": 125.75, "cidade": "Porto"},
    {"hotel_id": "fukui", "nome": "Hotel Fukui Paradise", "estrelas": 4.9, "diaria": 225.75, "cidade": "Lisboa"},
    {"hotel_id": "saint", "nome": "Resort Saint", "estrelas": 4.3, "diaria": 165.75, "cidade": "Coimbra"}
]

class Hoteis(Resource):
    def get(self):
        return { "hoteis": hoteis }
    
class Hotel(Resource):
    argumentos = reqparse.RequestParser() 
    argumentos.add_argument("nome", type=str, required=True, help="O nome do Hotel é Obrigatório")
    argumentos.add_argument("estrelas", type=float, required=True, help="Estrelas é Obrigatório")
    argumentos.add_argument("diaria", type=float, required=True, help="Diária do Hotel é Obrigatório")
    argumentos.add_argument("cidade", type=str, required=True, help="Cidade do Hotel é Obrigatório")

    def encontrar_Hotel(self, hotel_id):
        for hotel in hoteis:
            if hotel["hotel_id"] == hotel_id:
                return hotel
            return None
        
    def get(self, hotel_id):
        hotel = self.encontrar_Hotel(hotel_id)
        if hotel is not None:
            return hotel, 200
        return {"mensagem": "Hotel não foi encontrado"}

    def post(self, hotel_id):
        dados = Hotel.argumentos.parse_args() 

        hotel = self.encontrar_Hotel(hotel_id)
        if hotel is not None:
            return { "mensagem": f"O hotel com id {hotel_id} ja existe na minha lista."}
            
        novo_hotel = {"hotel_id": hotel_id, **dados}
        hoteis.append(novo_hotel)
        return novo_hotel, 200

    #Atualizar um hotel
    def put(self, hotel_id):
        dados = Hotel.argumentos.parse_args()

        hotel = self.encontrar_Hotel(hotel_id)
        if hotel is not None:
            hotel.update(dados)
            return hotel, 200
        
        novo_hotel = {"hotel_id": hotel_id, **dados}
        hoteis.append(novo_hotel)
        return novo_hotel, 201
    
    def delete(self,hotel_id):
        global hoteis
        hoteis = [hotel for hotel in hoteis if hotel["hotel_id"] != hotel_id]
        return {"mensagem": f"O hotel com id {hotel_id} foi removido com sucesso"}
