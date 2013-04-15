# Makefile for temper1

CC=gcc
CFLAGS=-c -Wall
LDFLAGS=-lusb
SOURCES=temper1.c usbhelper.c sysfshelper.c strreplace.c
DEPS=usbhelper.h sysfshelper.h strreplace.h
OBJECTS=$(SOURCES:.c=.o)
EXECUTABLE=temper1

all: $(SOURCES) $(EXECUTABLE)
	
$(EXECUTABLE): $(OBJECTS) 
	$(CC) -o $@ $(OBJECTS) $(LDFLAGS) 

%.o: %.c $(DEPS)
	$(CC) $(CFLAGS) $< -o $@

install:
	/bin/mkdir -p $(DESTDIR)/usr/bin
	/bin/mkdir -p $(DESTDIR)/usr/local/bin
	/bin/mkdir -p $(DESTDIR)/etc/temper
	/bin/mkdir -p $(DESTDIR)/lib/udev/rules.d
	/usr/bin/install -m 0755 -t $(DESTDIR)/usr/bin temper1
	/usr/bin/install -m 0755 -t $(DESTDIR)/usr/local/bin get_temps.sh
	/usr/bin/install -m 0644 temper1.conf.sample $(DESTDIR)/etc/temper/temper1.conf
	/usr/bin/install -m 0644 -t $(DESTDIR)/lib/udev/rules.d 60-temper.rules

clean:
	rm -f $(OBJECTS) $(EXECUTABLE)

