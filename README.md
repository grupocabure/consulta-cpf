# Consulta CPF Serpro

## Uso

1. Atualizar token de api com o seguinte comando (token basico conforme documentação da SERPRO, salvo no gerenciador de senhas):

```sh
curl -k -H "Authorization: Basic {TOKEN_BASICO}" -d "grant_type=client_credentials" https://gateway.apiserpro.serpro.gov.br/token
```
