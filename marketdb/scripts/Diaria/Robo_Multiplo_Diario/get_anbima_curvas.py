def robo_anbima_curvas():
    
    ###############################################################
    #
    #                   Informações da Anbima
    #
    ###############################################################
    
    import pandas as pd
    
    ###
    ### Curvas
    ###
    
    
    pagina_curvas_anbima="http://www.anbima.com.br/est_termo/CZ.asp"
    
    dados_curvas_anbima = pd.read_html(pagina_curvas_anbima, thousands=".")
    dados_curvas_anbima=dados_curvas_anbima[4]
    
    
    #Padronizar nomes das colunas e colocar data_referencia
    data_referencia=dados_curvas_anbima.columns[0]
    
    dados_curvas_anbima.columns=[
    "tipo",
    "beta1",
    "beta2",
    "beta3",
    "beta4",
    "lambda1",
    "lambda2"
    ]
    
    dados_curvas_anbima["data_referencia"]=datetime.datetime.strptime(data_referencia, "%d/%m/%Y").strftime('%Y-%m-%d')
    
    
    ## Criar coluna com data_bd para a data de inserção no BD
    horario_bd=datetime.datetime.now()
    dados_curvas_anbima["data_bd"]=horario_bd
    
    ## Trocar virgula por ponto e "--"/nan por None
    
    dados_curvas_anbima=dados_curvas_anbima.replace({',':'.'}, regex=True)
    
    # Salvar na base de dados
   
    connection=db.connect('localhost', user = 'root', passwd = senhabd, db = 'projeto_inv')
    
    pd.io.sql.to_sql(dados_curvas_anbima, name='anbima_parametros_nss', con=connection,if_exists="append", flavor='mysql', index=0)
    
#######################################################################################################
    