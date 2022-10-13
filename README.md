## Docker-compose
To run the docker-compose file, you need to have docker and docker-compose installed on your machine.

``` 
    docker-compose -f docker-compose.yml up
```

# KAFKA-CC

![Kafka img](images/kafka.png?raw=true "Kafka")
![Kafka img2](images/kafka2.png?raw=true "Kafka2")

## Topics
A topic is a category or feed name to which records are published. Topics in Kafka are always multi-subscriber; that is, a topic can have zero, one, or many consumers that subscribe to the data written to it. A topic is identified by its name, which must be unique within a Kafka cluster. A topic is either configured to be retained forever or to be deleted after a certain time has elapsed.

![Kafka img3](images/topic.png?raw=true "Kafka3")

- Kafka is a distributed streaming platform. It is used for building real-time data pipelines and streaming apps. It is horizontally scalable, fault-tolerant, wicked fast, and runs in production in thousands of companies.

## Kafka topic partition
A topic is split into a number of partitions, which are distributed over the brokers in the cluster. Each partition is an ordered, immutable sequence of records that is continually appended to—a commit log. The records in the partitions are each assigned a sequential id number called the offset that uniquely identifies each record within the partition. Kafka uses this mechanism to provide the features and services described below.

![Kafka img4](images/partition.png?raw=true "Kafka4")

## Kafka Producer
A Kafka producer is a client that publishes records to the Kafka cluster. The producer is responsible for choosing which record will be assigned to which partition within the topic. If no partition is specified in the record, then the producer will use a partitioner to choose one. The partition is chosen by applying a hash function to the key of the record, or if the key is null then the producer will choose a partition in a round-robin fashion.

## Kafka Consumer
A Kafka consumer is a client that subscribes to a topic and processes the records that it receives. The consumer can either read the records in order, which is the default behavior, or skip around in the partition to consume only records that meet a certain filter criterion.

![Kafka img9](images/kafka3.png?raw=true "Kafka9")

## Kafka Consumer Group
A consumer group is a group of consumers that work together to consume messages from a Kafka topic. Each consumer in a group is assigned a subset of the partitions in the topic. The consumer group as a whole is responsible for consuming all the messages in the topic. If there are more partitions in the topic than there are consumers in the group, then some consumers will be assigned multiple partitions. If there are fewer partitions in the topic than there are consumers in the group, then some consumers will not be assigned any partitions.

![Kafka img10](images/kafka4.png?raw=true "Kafka10")

A consumer instance of same consumer group can be deployed on different machines. This is useful when you want to scale your consumer. You can add more instances of same consumer group to consume more messages.

![Kafka img11](images/kafka5.png?raw=true "Kafka11")

## Kafka replication

![Kafka img5](images/kafka6.png?raw=true "Kafka5")

Kafka replicates data across multiple servers to prevent data loss in case of hardware failure. Replication is a key feature of Kafka that makes it fault tolerant. Replication is also used to provide high availability. Replication is asynchronous. This means that the leader does not wait for the followers to acknowledge the receipt of the data before responding to the producer. This allows the producer to continue to send data to the leader without waiting for the acknowledgement from the followers. The leader will periodically send a message to the followers to check if they are still alive. If the leader does not receive a response from a follower within a certain period of time, it will mark the follower as dead and stop sending it messages. The leader will then reassign the partitions that were being hosted on the dead follower to one of the alive followers.

## Round Robin Partition Assignment
The default partition assignment strategy is round robin. This strategy assigns partitions to consumers in a round robin fashion. For example, if there are 3 consumers in a consumer group and 5 partitions in a topic, then the first consumer will be assigned partitions 0, 3, and 1, the second consumer will be assigned partitions 4 and 2, and the third consumer will be assigned partitions 0, 3, and 1.
## Kafka in python

### bootstrap_servers
A list of host/port pairs to use for establishing the initial connection to the Kafka cluster. This does not have to be the full node list. It just needs to have at least one broker that will respond to a Metadata API Request. The default port is 9092. If no servers are specified, it will default to localhost:9092.

### value_serializer
A function used to encode message values prior to serialization. If None, message values will be sent as raw bytes.

```
    pip install kafka-python # install kafka-python
    pip install faker # install faker for fake data
```

![Kafka img5](images/kafkaPython.png?raw=true "Kafka5")

# Zookeeper and Confluent

- Zookeeper is a centralized service for maintaining configuration information, naming, providing distributed synchronization, and providing group services. All of these kinds make it a perfect fit for Kafka.

- Confluent is a company that provides a distribution of Apache Kafka that includes additional enterprise features and support. Confluent is the company behind the Kafka project and the Kafka community.

# Kafka Connect

- Kafka Connect is a tool for scalably and reliably streaming data between Apache Kafka and other systems. It is a framework for connecting Kafka with external systems such as databases, key-value stores, search indexes, and file systems.

# Kafka Streams

- Kafka Streams is a client library for building applications and microservices, where the input and output data are stored in Kafka clusters. It builds upon important stream processing concepts such as properly distinguishing between event time and processing time, windowing support, and simple yet efficient management of application state.

# Kafka REST Proxy

- The Kafka REST Proxy provides a RESTful interface to a Kafka cluster. It makes it easy to produce and consume messages, view the state of the cluster, and perform administrative actions without using the native Kafka protocol or clients.

# Kafka KSQL

- KSQL is an open-source streaming SQL engine for Apache Kafka. It provides a simple SQL-like language for writing streaming applications on top of Kafka. KSQL is a great tool for building streaming applications on top of Kafka.

## Concepts and Producer Example 1

![Kafka img6](images/example1.png?raw=true "Kafka6")

## Concepts and Producer Example 2
![Kafka img7](images/example2.png?raw=true "Kafka7")

## Concepts and Producer Example 3
![Kafka img8](images/example3.png?raw=true "Kafka8")

## Concepts and Consumer Example 1
![Kafka img12](images/example4.png?raw=true "Kafka12")

## Concepts and Consumer Example 2
![Kafka img13](images/example5.png?raw=true "Kafka13")

## Concepts and Consumer Example 3
In this example, in order to simulate 2 consumers, we will run 2 different terminals and run the consumer.py file in each of them.

![Kafka img14](images/example6.png?raw=true "Kafka14")

All messages are consumed by one of the consumers because we have only one partition. If we have more partitions, then messages will be consumed by different consumers.

![Kafka img15](images/example7.png?raw=true "Kafka15")

If we change consumer group id in one of the consumers, then all messages will be consumed by both consumers. because we have 2 different consumer groups.

## Concepts and Consumer Example 4

![Kafka img16](images/example8.png?raw=true "Kafka16")

## Concepts and Replication Example 5

This example only shows one leader partition.

![Kafka img17](images/example9.png?raw=true "Kafka17")

The next example has 2 replicas one of them is leader and the other is follower.

![Kafka img18](images/example10.png?raw=true "Kafka18")

The next example has 3 replicas one of them is leader and the other 2 are followers.

![Kafka img19](images/example11.png?raw=true "Kafka19")

Zookeper knows which broker is leader and which one is follower.