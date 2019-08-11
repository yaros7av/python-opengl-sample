import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
import PIL.Image
import numpy as np

# (<x>, <y>, <z>)
from pygame.tests.test_utils.png import Image

def loadTexture(filename):
    """load OpenGL 2D texture from given image file"""
    img = PIL.Image.open(filename)
    print("loaded image: %s with size: %s" % (filename, str(img.size)))
    dur = list(img.getdata())
    img_data = np.array(dur, dtype=np.uint8)
    glEnable(GL_TEXTURE_2D)
    texture = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, img.size[0], img.size[1], 0, GL_RGB, GL_UNSIGNED_BYTE, img_data)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR)
    glGenerateMipmap(GL_TEXTURE_2D)
    return texture

def cube():
    glBegin(GL_QUADS);
    glTexCoord2f(0.0, 0.0);
    glVertex3f(-1.0, -1.0, 1.0);
    glTexCoord2f(1.0, 0.0);
    glVertex3f(1.0, -1.0, 1.0);
    glTexCoord2f(1.0, 1.0);
    glVertex3f(1.0, 1.0, 1.0);
    glTexCoord2f(0.0, 1.0);
    glVertex3f(-1.0, 1.0, 1.0);
    glTexCoord2f(1.0, 0.0);
    glVertex3f(-1.0, -1.0, -1.0);
    glTexCoord2f(1.0, 1.0);
    glVertex3f(-1.0, 1.0, -1.0);
    glTexCoord2f(0.0, 1.0);
    glVertex3f(1.0, 1.0, -1.0);
    glTexCoord2f(0.0, 0.0);
    glVertex3f(1.0, -1.0, -1.0);
    glTexCoord2f(0.0, 1.0);
    glVertex3f(-1.0, 1.0, -1.0);
    glTexCoord2f(0.0, 0.0);
    glVertex3f(-1.0, 1.0, 1.0);
    glTexCoord2f(1.0, 0.0);
    glVertex3f(1.0, 1.0, 1.0);
    glTexCoord2f(1.0, 1.0);
    glVertex3f(1.0, 1.0, -1.0);
    glTexCoord2f(1.0, 1.0);
    glVertex3f(-1.0, -1.0, -1.0);
    glTexCoord2f(0.0, 1.0);
    glVertex3f(1.0, -1.0, -1.0);
    glTexCoord2f(0.0, 0.0);
    glVertex3f(1.0, -1.0, 1.0);
    glTexCoord2f(1.0, 0.0);
    glVertex3f(-1.0, -1.0, 1.0);
    glTexCoord2f(1.0, 0.0);
    glVertex3f(1.0, -1.0, -1.0);
    glTexCoord2f(1.0, 1.0);
    glVertex3f(1.0, 1.0, -1.0);
    glTexCoord2f(0.0, 1.0);
    glVertex3f(1.0, 1.0, 1.0);
    glTexCoord2f(0.0, 0.0);
    glVertex3f(1.0, -1.0, 1.0);
    glTexCoord2f(0.0, 0.0);
    glVertex3f(-1.0, -1.0, -1.0);
    glTexCoord2f(1.0, 0.0);
    glVertex3f(-1.0, -1.0, 1.0);
    glTexCoord2f(1.0, 1.0);
    glVertex3f(-1.0, 1.0, 1.0);
    glTexCoord2f(0.0, 1.0);
    glVertex3f(-1.0, 1.0, -1.0);
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    loadTexture("test.bmp")

    glTranslatef(0.0, 0.0, -5)

    glRotatef(0, 0, 0, 0)

    shiftActive = 0
    ctrlActive = 0

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                  glTranslatef(0.03, 0, 0)
            if event.key == pygame.K_RIGHT:
                  glTranslatef(-0.03, 0, 0)
            if event.key == pygame.K_UP:
                  glTranslatef(0, -0.03, 0)
            if event.key == pygame.K_DOWN:
                  glTranslatef(0, 0.03, 0)
            if event.key == pygame.K_LSHIFT:
                shiftActive = 1
            if event.key == pygame.K_LCTRL:
                ctrlActive = 1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LSHIFT:
                shiftActive = 0
            if event.key == pygame.K_LCTRL:
                ctrlActive = 0

        # scroll controls  !CURRENTLY IN CLIK MODE BECAUSE OF MOUSE ISSUES!
        if shiftActive:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    glTranslatef(-0.03, 0, 0)
                if event.button == 3:
                    glTranslatef(0.03, 0, 0)
        elif ctrlActive:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    glTranslatef(0, 0, 0.03)
                if event.button == 3:
                    glTranslatef(0, 0, -0.03)
        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    glTranslatef(0, -0.03, 0)
                if event.button == 3:
                    glTranslatef(0, 0.03, 0)

##        glRotatef(1, 1, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        cube()
        pygame.display.flip()
        pygame.time.wait(10)

main()
