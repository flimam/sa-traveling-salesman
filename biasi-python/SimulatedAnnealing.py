# -.- coding: utf8 -.-
import math, random
from Cidade import Cidade
from Viagem import Viagem

class SimulatedAnnealing():

	_lista = []
	_temperatura = 1000
	_resfriamento = 0.003

	def __init__(self, lista):
		self._lista = lista

	def aceitar(self, energia, nova_energia):
		if nova_energia < energia:
			return 1.0
		return math.exp((energia - nova_energia) / self._temperatura)

	def run(self):
		solucao_atual = Viagem()
		solucao_atual.gerar(self._lista)

		print u'Solução inicial: %f' % solucao_atual.get_total_distancia()

		melhor_solucao = Viagem(solucao_atual)

		while self._temperatura > 1:
			nova_solucao = Viagem(solucao_atual)

			pos1 = int((nova_solucao.tamanho() * random.random()))
			pos2 = int((nova_solucao.tamanho() * random.random()))

			c1 = nova_solucao.get_cidade(pos1)
			c2 = nova_solucao.get_cidade(pos2)

			nova_solucao.set_cidade(pos1, c2)
			nova_solucao.set_cidade(pos2, c1)

			energia_atual = solucao_atual.get_total_distancia()
			nova_energia = nova_solucao.get_total_distancia()

			if self.aceitar(energia_atual, nova_energia) > random.random():
				solucao_atual = nova_solucao
			
			if solucao_atual.get_total_distancia() < melhor_solucao.get_total_distancia():
				melhor_solucao = solucao_atual

			self._temperatura *= (1 - self._resfriamento)

		print 'Melhor distancia: %f' % (melhor_solucao.get_total_distancia())
		print 'Temperatura: %f' % (self._temperatura)
		print 'Tour:', melhor_solucao


if __name__ == '__main__':

	cidades = []
	
	cidades.append(Cidade(60, 200))
	cidades.append(Cidade(180, 200))
	cidades.append(Cidade(80, 180))
	cidades.append(Cidade(140, 180))
	cidades.append(Cidade(20, 160))
	cidades.append(Cidade(100, 160))
	cidades.append(Cidade(200, 160))
	cidades.append(Cidade(140, 140))
	cidades.append(Cidade(40, 120))
	cidades.append(Cidade(100, 120))
	cidades.append(Cidade(180, 110))
	cidades.append(Cidade(60, 80))
	cidades.append(Cidade(120, 80))
	cidades.append(Cidade(180, 60))
	cidades.append(Cidade(20, 40))
	cidades.append(Cidade(100, 40))
	cidades.append(Cidade(200, 40))
	cidades.append(Cidade(20, 20))
	cidades.append(Cidade(60, 20))
	cidades.append(Cidade(160, 20))

	task = SimulatedAnnealing(cidades)
	task.run()