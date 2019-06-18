# springboot-python

##
分别将eureka-server、java-service和sidecar倒入intellij，然后先进行mvn clean和mvn install
再运行
DemoApplication.java、RibbonConsumerApplication.java和SidecarApplication.java启动对应的服务；

##启动python服务
```
cd python && python sanic_server.py
```

## dir-tree
```
springboot-python
├── eureka-server
│   ├── mvnw
│   ├── pom.xml
│   ├── src
│   │   ├── main
│   │   │   ├── java
│   │   │   │   └── com
│   │   │   │       └── example
│   │   │   │           └── demo
│   │   │   │               └── DemoApplication.java
│   │   │   └── resources
│   │   │       └── application.properties
│   │   └── test
│   │       └── java
│   │           └── com
│   │               └── example
│   │                   └── demo
│   │                       └── DemoApplicationTests.java
├── java-service
│   ├── mvnw
│   ├── pom.xml
│   ├── src
│   │   └── main
│   │       ├── java
│   │       │   └── com
│   │       │       └── example
│   │       │           └── demo
│   │       │               ├── JavaController.java
│   │       │               └── RibbonConsumerApplication.java
│   │       └── resources
│   │           └── application.properties
├── python
│   └── sanic_server.py
├── README.md
└── sidecar
    ├── pom.xml
    ├── src
    │   ├── main
    │   │   ├── java
    │   │   │   └── com
    │   │   │       └── kaozhao
    │   │   │           └── SidecarApplication.java
    │   │   └── resources
    │   │       └── application.properties
    │   └── test
    │       └── java
    │           └── com
    │               └── kaozhao
    │                   └── SidecarApplicationTests.java
```
