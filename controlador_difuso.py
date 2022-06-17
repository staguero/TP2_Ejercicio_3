class controlador_difuso():
    def __init__(self,dominio):
        self.dominio=dominio
        self.conjuntos_borrosos=list

    def particion_difusa(self): #NG NP Z PP PG
        intervalo=(self.dominio[1]-self.dominio[0])/6
        Z=[-intervalo,intervalo]
        PP=[0,2*intervalo]
        PG=[intervalo,self.dominio[1]]
        NP=[-2*intervalo,0]
        NG=[self.dominio[0],-intervalo]
        self.conjuntos_borrosos=[NG,NP,Z,PP,PG]
        
        return self.conjuntos_borrosos

    def borrosificar(self,valor_entorno): #Calcula el valor de pertenencia
        valor_pertenencia=[0,0,0,0,0]
        posicion_en_vp=0

        for conjunto_borroso in self.conjuntos_borrosos:
            ext_izq=conjunto_borroso[0]
            ext_der=conjunto_borroso[1]
            centro=(ext_der+ext_izq)/2
            
            if valor_entorno<ext_izq:
                valor_pertenencia[posicion_en_vp]=0
            
            if ext_izq<=valor_entorno<=centro:
                if posicion_en_vp==0:
                    valor_pertenencia[0]=1
                else:
                    valor_pertenencia[posicion_en_vp]=(valor_entorno-ext_izq)/(centro-ext_izq)
            
            if centro<valor_entorno<=ext_der:
                if posicion_en_vp==4:
                    valor_pertenencia[4]=1
                else:
                    valor_pertenencia[posicion_en_vp]=(valor_entorno-ext_der)/(centro-ext_der)
            
            if valor_entorno>ext_der:
                valor_pertenencia[posicion_en_vp]=0
            
            posicion_en_vp+=1
        
        return valor_pertenencia

    def fam(self,theta_cb,omega_cb): #cb: con borrosificacion
        F=[0,0,0,0,0] #NG(0),NP(1),Z(2),PP(3),PG(4)
        #Columna 0
        if theta_cb[0]!=0 and omega_cb[0]!=0:
            conjuncion=min(theta_cb[0],omega_cb[0])
            F[4]=max(conjuncion,F[4]) #disyuncion
        if theta_cb[0]!=0 and omega_cb[1]!=0:
            conjuncion=min(theta_cb[0],omega_cb[1])
            F[4]=max(conjuncion,F[4]) #disyuncion
        if theta_cb[0]!=0 and omega_cb[2]!=0:
            conjuncion=min(theta_cb[0],omega_cb[2])
            F[4]=max(conjuncion,F[4]) #disyuncion
        if theta_cb[0]!=0 and omega_cb[3]!=0:
            conjuncion=min(theta_cb[0],omega_cb[3])
            F[3]=max(conjuncion,F[3]) #disyuncion
        if theta_cb[0]!=0 and omega_cb[4]!=0:
            conjuncion=min(theta_cb[0],omega_cb[4])
            F[2]=max(conjuncion,F[2]) #disyuncion
        
        #Columna 1
        if theta_cb[1]!=0 and omega_cb[0]!=0:
            conjuncion=min(theta_cb[1],omega_cb[0])
            F[4]=max(conjuncion,F[4]) #disyuncion
        if theta_cb[1]!=0 and omega_cb[1]!=0:
            conjuncion=min(theta_cb[1],omega_cb[1])
            F[4]=max(conjuncion,F[4]) #disyuncion
        if theta_cb[1]!=0 and omega_cb[2]!=0:
            conjuncion=min(theta_cb[1],omega_cb[2])
            F[3]=max(conjuncion,F[3]) #disyuncion
        if theta_cb[1]!=0 and omega_cb[3]!=0:
            conjuncion=min(theta_cb[1],omega_cb[3])
            F[2]=max(conjuncion,F[2]) #disyuncion
        if theta_cb[1]!=0 and omega_cb[4]!=0:
            conjuncion=min(theta_cb[1],omega_cb[4])
            F[4]=max(conjuncion,F[4]) #disyuncion

        #Columna 2
        if theta_cb[2]!=0 and omega_cb[0]!=0:
            conjuncion=min(theta_cb[2],omega_cb[0])
            F[4]=max(conjuncion,F[4]) #disyuncion
        if theta_cb[2]!=0 and omega_cb[1]!=0:
            conjuncion=min(theta_cb[2],omega_cb[1])
            F[4]=max(conjuncion,F[4]) #disyuncion
        if theta_cb[2]!=0 and omega_cb[2]!=0:
            conjuncion=min(theta_cb[2],omega_cb[2])
            F[2]=max(conjuncion,F[2]) #disyuncion
        if theta_cb[2]!=0 and omega_cb[3]!=0:
            conjuncion=min(theta_cb[2],omega_cb[3])
            F[1]=max(conjuncion,F[1]) #disyuncion
        if theta_cb[2]!=0 and omega_cb[4]!=0:
            conjuncion=min(theta_cb[2],omega_cb[4])
            F[0]=max(conjuncion,F[0]) #disyuncion
        
        #Columna 3
        if theta_cb[3]!=0 and omega_cb[0]!=0:
            conjuncion=min(theta_cb[3],omega_cb[0])
            F[3]=max(conjuncion,F[3]) #disyuncion
        if theta_cb[3]!=0 and omega_cb[1]!=0:
            conjuncion=min(theta_cb[3],omega_cb[1])
            F[2]=max(conjuncion,F[2]) #disyuncion
        if theta_cb[3]!=0 and omega_cb[2]!=0:
            conjuncion=min(theta_cb[3],omega_cb[2])
            F[1]=max(conjuncion,F[1]) #disyuncion
        if theta_cb[3]!=0 and omega_cb[3]!=0:
            conjuncion=min(theta_cb[3],omega_cb[3])
            F[0]=max(conjuncion,F[0]) #disyuncion
        if theta_cb[3]!=0 and omega_cb[4]!=0:
            conjuncion=min(theta_cb[3],omega_cb[4])
            F[0]=max(conjuncion,F[0]) #disyuncion

        #Columna 4
        if theta_cb[4]!=0 and omega_cb[0]!=0:
            conjuncion=min(theta_cb[4],omega_cb[0])
            F[2]=max(conjuncion,F[2]) #disyuncion
        if theta_cb[4]!=0 and omega_cb[1]!=0:
            conjuncion=min(theta_cb[4],omega_cb[1])
            F[0]=max(conjuncion,F[0]) #disyuncion
        if theta_cb[4]!=0 and omega_cb[2]!=0:
            conjuncion=min(theta_cb[4],omega_cb[2])
            F[0]=max(conjuncion,F[0]) #disyuncion
        if theta_cb[4]!=0 and omega_cb[3]!=0:
            conjuncion=min(theta_cb[4],omega_cb[3])
            F[0]=max(conjuncion,F[0]) #disyuncion
        if theta_cb[4]!=0 and omega_cb[4]!=0:
            conjuncion=min(theta_cb[4],omega_cb[4])
            F[0]=max(conjuncion,F[0]) #disyuncion
        
        return F

    def desborrosificador(self,fuerza_difusa):
        numerador=0
        denominador=sum(fuerza_difusa)
        if denominador!=0:
            for i in range(0,5):
                conjunto_borroso=self.conjuntos_borrosos[i]
                centro=(conjunto_borroso[0]+conjunto_borroso[1])/2
                numerador=(centro*fuerza_difusa[i])+numerador
            valor_fuerza=numerador/denominador
        else:
            valor_fuerza=0

        return valor_fuerza