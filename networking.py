import socket

def recv_msg(conn):
    """
    Receives a message from the socket.
    """
    try:
        # Unwrap message length header
        header = conn.recv(8).decode("UTF-8")
        length = int(header)
        body = conn.recv(length)
        return body
    except:
        raise IOError()
        return None
    
def recv_str(conn):
    """
    Convenience method for reading a string
    from the socket.
    """
    return recv_msg(conn).decode("UTF-8")

def send_msg(conn, msg):
    """
    Sends a message out the socket.
    """
    try:
        # Prepend message length header
        length = len(msg)
        msg = bytes(str(length).ljust(8), "UTF-8") + msg
        conn.send(msg)
    except:
        raise IOError()
        return None
    
def send_str(conn, msg):
    """
    Convenience method for sending a string
    out the socket.
    """
    length = len(msg)
    msg = bytes(str(length).ljust(8), "UTF-8") + bytes(msg, "UTF-8")
    conn.send(msg)
    
def broadcast_mst(conns, msg):
    """
    Sends a message out to all given connections
    """
    for conn in conns:
        send_msg(conn, msg)
        
def broadcast_str(conns, msg):
    """
    Convenience method for broadcasting a string
    out the given list of sockets.
    """
    for conn in conns:
        send_str(conn, msg)
    